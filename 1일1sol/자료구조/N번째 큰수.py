import sys
from heapq import heappop,heappush

n = int(sys.stdin.readline())
pq = []
for _ in range(n):
    numbers = list(map(int,sys.stdin.readline().strip().split(' ')))
    for num in numbers:

        if len(pq) < n:
            heappush(pq,num)
        else:
            if pq[0] < num:
                heappop(pq)
                heappush(pq, num)


print(pq[0])