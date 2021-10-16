import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)
n, m, x, y = map(int, sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]
dp = [sys.maxsize for _ in range(n+1)]
path = [-1 for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))


# 최단 경로
def dijkstra(start):
    queue = []
    dp[start] = 0
    heapq.heappush(queue,(0,start))

    while queue:
        distance,current = heapq.heappop(queue)
        if dp[current] < distance:
            continue
        for next, weight in adjlist[current]:
            if dp[next] > dp[current] + weight:
                dp[next] = dp[current] + weight
                heapq.heappush(queue,(dp[next],next))

    return
#path길이 구하기
def Dijkstra(start):

    path[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for next, weight in adjlist[cur]:
            if dp[cur] + weight != dp[next]:
                continue
            if path[next] == -1:
                path[next] = path[cur] + 1
                queue.append(next)

    return


count = [-1 for _ in range(n+1)]
count[y] = 1
def CountNode(cur):


    if count[cur] != -1:
        return count[cur]
    count[cur] = 0
    for next,weight in adjlist[cur]:
        if dp[cur] + weight == dp[next] and path[cur] + 1 == path[next]:
            count[cur] = (count[cur]+CountNode(next)) % (10**9 + 9)

    return count[cur]

dijkstra(x)
Dijkstra(x)
if dp[y] == sys.maxsize:
    print(-1)
else:
    print(dp[y])
    print(path[y])
    CountNode(x)
    print(count[x])
