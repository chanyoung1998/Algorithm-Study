import sys
from heapq import heappop,heappush

n = int(sys.stdin.readline())
time = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    time.append((s, t))

time.sort(key=lambda x: x[0])
pq = []

for s,t in time:
    if pq:
        pt,ps = heappop(pq)
        if pt <= s:
            heappush(pq,(t,s))
        else:
            heappush(pq,(t,s))
            heappush(pq,(pt,ps))

    else:
        heappush(pq,(t,s))


print(len(pq))
