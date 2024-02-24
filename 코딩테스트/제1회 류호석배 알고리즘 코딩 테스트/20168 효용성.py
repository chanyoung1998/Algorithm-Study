# 시작 점으로부터 도착점까지 가는동안 내야하는 "최대 요금의 최솟값"을 구해야 하는데 이는 흔히
# 이분탐색에서 자주 나타나는 "최대의 최소화"꼴입니다.
import sys
import heapq
sys.setrecursionlimit(10**5 + 1)
n,m,a,b,c = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))
    adjlist[v].append((u,w))

def sol():
    left = 0
    right = 10**9
    ans = sys.maxsize
    while left <= right:
        mid = (left+right)//2

        if check(mid):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1

    if ans != sys.maxsize:
        print(ans)
    else:
        print(-1)

def check(max):
    dist = [sys.maxsize for _ in range(n + 1)]
    q = []
    heapq.heappush(q,(0,a))
    dist[a] = 0

    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance:
            continue

        for next, weight in adjlist[now]:

            if weight <= max and distance + weight < dist[next]:
                dist[next] = distance + weight
                heapq.heappush(q,(dist[next],next))


    return dist[b] <= c

sol()