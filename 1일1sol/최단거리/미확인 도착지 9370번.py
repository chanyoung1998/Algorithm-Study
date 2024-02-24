import sys
from heapq import heappop,heappush

testcase = int(sys.stdin.readline())
INF = sys.maxsize

def dijkstra(start):
    pq = []
    dist = [INF for _ in range(n + 1)]
    path = [None for _ in range(n + 1)]
    dist[start] = 0
    heappush(pq, (dist[start], start))

    while pq:

        dist_cur, cur = heappop(pq)

        if dist_cur > dist[cur]:
            continue

        for next, weight in adj[cur]:

            if dist[next] > dist_cur + weight:
                dist[next] = dist_cur + weight
                path[next] = cur
                heappush(pq, (dist[next], next))

    return dist

for _ in range(testcase):
    n,m,t = map(int,sys.stdin.readline().rstrip().split())
    s,g,h = map(int,sys.stdin.readline().rstrip().split())
    adj = [[] for _ in range(n+1)]

    for _  in range(m):
        u,v,w = map(int,sys.stdin.readline().rstrip().split())
        adj[u].append((v,w))
        adj[v].append((u,w))

    cand = []

    for _ in range(t):
        cand.append(int(sys.stdin.readline()))

    # s - g - h - > 후보지
    # s - h - g - > 후보지
    gh_W = None
    for next,weight in adj[g]:
        if next == h:
            gh_W = weight
            break

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    ret = []
    for cross in cand:
        if dist_s[g] +gh_W + dist_h[cross] == dist_s[cross] or \
            dist_s[h] +gh_W + dist_g[cross] == dist_s[cross]:
            ret.append(cross)


    ret.sort()
    print(*ret)