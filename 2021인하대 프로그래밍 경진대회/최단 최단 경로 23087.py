import sys
import heapq
n, m, x, y = map(int, sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]
dp = [sys.maxsize for _ in range(n+1)]
path = [sys.maxsize for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))


# 최단 경로와 목적지 까지 가는데 필요한 경로의 개수 구하기
def dijkstra(start):
    queue = []
    dp[start] = 0
    path[start] = 0
    heapq.heappush(queue,(0,start))

    while queue:
        distance,current = heapq.heappop(queue)
        if dp[current] < distance:
            continue
        for next, weight in adjlist[current]:
            if dp[next] > dp[current] + weight:
                dp[next] = dp[current] + weight
                path[next] = path[current] + 1
                heapq.heappush(queue,(dp[next],next))
    return


def CountNode(start):

    count = [0 for _ in range(n + 1)]
    visit = [False for _ in range(n+1)]
    count[start] = 1
    queue = []
    heapq.heappush(queue,start)

    while queue:
        cur = heapq.heappop(queue)
        if visit[cur]:
            continue
        visit[cur] = True
        for next,weight in adjlist[cur]:
            if dp[cur] + weight == dp[next] and path[cur] + 1 == path[next]:
                count[next] += count[cur]
                count[next] %= 10 ** 9 + 9
                heapq.heappush(queue,next)


    #print(count)
    return count[y] % (10**9 + 9)

dijkstra(x)
if dp[y] == sys.maxsize:
    print(-1)
else:
    print(dp[y])
    print(path[y])
    print(CountNode(x))
