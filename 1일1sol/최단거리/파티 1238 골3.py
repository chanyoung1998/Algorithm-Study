'''
24 02 22
파티 1238
골3
최단거리, 다익스트라
'''

import sys
from heapq import heappush,heappop
def solve(a):
    pq = []
    distance = [sys.maxsize for _ in range(n + 1)]
    heappush(pq, (0, a))
    distance[a] = 0

    while pq:
        cost, cur = heappop(pq)

        if distance[cur] < cost:
            continue

        for (next, time) in adjlist[cur]:
            if distance[next] > time + cost:
                distance[next] = time + cost
                heappush(pq, (distance[next], next))

    return distance

n, m, x = map(int, sys.stdin.readline().strip().split(' '))
adjlist = [[] for _ in range(n + 1)]
for _ in range(m):
    u, w, t = map(int, sys.stdin.readline().strip().split(' '))
    adjlist[u].append((w, t))


ret = [0 for _ in range(n+1)]
for i in range(1,n+1):
    distance = solve(i)
    ret[i] = distance[x]

distance = solve(x)

for i in range(1,n+1):
    ret[i] += distance[i]

print(max(ret))



