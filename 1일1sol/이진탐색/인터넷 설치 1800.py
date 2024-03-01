'''
24 02 28
인터넷 설치
1800
골1
이분탐색
'''
import sys
from heapq import heappush,heappop

n, p, k = map(int, sys.stdin.readline().strip().split(' '))
adjlist = [[] for _ in range(n + 1)]

for _ in range(p):
    a, b, c = map(int, sys.stdin.readline().strip().split(' '))
    adjlist[a].append((b, c))
    adjlist[b].append((a, c))


def checkDijkstra(target):
    visit = [sys.maxsize for _ in range(n + 1)]

    pq = []
    heappush(pq,(0, 1))
    visit[1] = 0

    while pq:

        curCost, cur = heappop(pq)

        if visit[cur] < curCost:
            continue

        for next, nextCost in adjlist[cur]:

            if nextCost <= target:
                c = 0
            else:
                c = 1

            if visit[next] > curCost + c:
                visit[next] = curCost + c
                heappush(pq,(visit[next],next))
    if visit[n] <= k:
        return True
    else:
        return False


low = -1
high = 1000000

while low + 1 < high:
    mid = (low + high) // 2

    if checkDijkstra(mid):
        high = mid
    else:
        low = mid


print(high)
