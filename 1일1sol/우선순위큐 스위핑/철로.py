import sys
from heapq import heappop,heappush

n = int(sys.stdin.readline())
coord = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    if a > b:
        a,b = b,a
    coord.append((a,b))
l = int(sys.stdin.readline())
coord.sort(key=lambda x:(x[1],x[0]))
pq = []
ret = 0
for x,y in coord:

    if x < y -l:
        continue


    while pq:
        if y-l <= pq[0][0]:
            break
        else:
            heappop(pq)

    heappush(pq, (x, y))

    ret = max(ret,len(pq))

print(ret)