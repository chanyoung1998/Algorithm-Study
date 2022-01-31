import sys
from heapq import heappush,heappop

n,l = map(int,sys.stdin.readline().rstrip().split())
arrays = list(map(int,sys.stdin.readline().rstrip().split()))
pq = []
for i in range(n):
    # heappush(pq, (arrays[i], i))
    #
    # pos = pq[0][1]
    # while pos < i - l + 1:
    #     heappop(pq)
    #     pos = pq[0][1]
    #
    # print(pq[0][0],end=' ')

    while pq and pq[0][1] < i - l + 1:
        heappop(pq)
    heappush(pq,(arrays[i],i))
    print(pq[0][0], end=' ')