import sys
from heapq import heappop,heappush

n,m = map(int,sys.stdin.readline().strip().split(' '))
cards = list(map(int,sys.stdin.readline().strip().split(' ')))
pq = []
for c in cards:
    heappush(pq,c)

for _ in range(m):
    a = heappop(pq)
    b = heappop(pq)

    heappush(pq,a+b)
    heappush(pq,a+b)

print(sum(pq))