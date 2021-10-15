import sys
import heapq
n, m, x, y = map(int, sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]
dp = [sys.maxsize for _ in range(n+1)]
path = [sys.maxsize for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))


def dijkstra(start):
    queue = []
    dp[start] = 0
    path[start] = 0
    heapq.heappush(queue,(0,start))
    ret = 0

    while queue:
        distance,current = heapq.heappop(queue)
        if dp[current] < distance:
            continue
        for next,weight in adjlist[current]:
            if dp[next] > dp[current] + weight:

                if next == y:
                    if dp[next] == dp[current] + weight and path[next] == path[current] + 1:
                        ret += 1
                    elif dp[next] == dp[current] + weight and path[next] > path[current] + 1:
                        ret = 1
                    elif dp[next] > dp[current] + weight:
                        ret = 1

                dp[next] = dp[current] + weight
                path[next] = path[current] + 1
                heapq.heappush(queue,(dp[next],next))

    return ret


ret1 = dijkstra(x)
if dp[y] == sys.maxsize:
    print(-1)
else:
    print(dp[y])
    print(path[y])
    print(ret1 % (10**9 + 9))