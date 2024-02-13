import sys
from heapq import heappop,heappush

def solution(n, edges):
    answer = 0

    adjlist = [[] for _ in range(n+1)]

    for edge in edges:
        a = edge[0]
        b = edge[1]
        adjlist[a].append(b)
        adjlist[b].append(a)

    dist = dijkstra(n,adjlist)
    maxDist = 0
    for d in dist:
        if d != sys.maxsize and maxDist < d:
            maxDist = d

    answer = dist.count(maxDist)

    return answer

def dijkstra(n,adjlist):

    dist = [sys.maxsize for _ in range(n+1)]

    start = 1
    dist[start] = 0

    pq = []
    heappush(pq,(0,start))

    while pq:

        curDist, curNode = heappop(pq)
        if curDist > dist[curNode]:
            continue

        for nextNode in adjlist[curNode]:
            if dist[nextNode] > curDist + 1:
                dist[nextNode] = curDist + 1
                heappush(pq,(curDist+1,nextNode))

    return dist

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))








