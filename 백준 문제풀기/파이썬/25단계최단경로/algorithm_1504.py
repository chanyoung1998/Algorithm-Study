'''
내용:백준 알고리즘 단계별 풀기 최단 경로 1504번 특정한 최단 경로
날짜:21년4월 11일
사용 언어:파이썬
'''

import sys
import heapq

n, e = map(int, sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adjlist[a].append((b,c))
    adjlist[b].append((a,c))

v1, v2 = map(int, sys.stdin.readline().rstrip().split())

def dijkstra(start):
    distance = [sys.maxsize for _ in range(n+1)]
    visited = [False for _ in range(n + 1)]
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))

    while heap:

        wei, cur = heapq.heappop(heap)
        if visited[cur]:
            continue

        visited[cur] = True
        for edge, weight in adjlist[cur]:
            if distance[edge] > distance[cur] + weight:
                distance[edge] = distance[cur] + weight
                heapq.heappush(heap,(distance[edge],edge))

    return distance

distance_1 = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)

onetov1 = distance_1[v1]
v1tov2 = distance_v1[v2]
v2ton = distance_v2[n]

onetov2 = distance_1[v2]
v2tov1 = distance_v2[v1]
v1ton = distance_v1[n]

if (onetov1 == sys.maxsize or v1tov2 == sys.maxsize or v2ton == sys.maxsize) and (onetov2 == sys.maxsize or v2tov1 == sys.maxsize or v1ton == sys.maxsize):
    print(-1)
else:
    print(min(onetov1+v1tov2+v2ton,onetov2+v2tov1+v1ton))

