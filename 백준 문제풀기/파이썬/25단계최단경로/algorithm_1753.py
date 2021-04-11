'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 1753 최단경로
날짜:21년4월 11일
사용 언어:파이썬
'''

import sys
import heapq
V, E = map(int,sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())
adjlist = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))

def dijkstra(start):
    distance = [sys.maxsize for _ in range(V+1)]
    distance[start] = 0
    heap = []
    for i in range(1,V+1):
        heapq.heappush(heap,(distance[i],i))

    for i in range(V-2):
        min_vertex = heapq.heappop(heap)[1]
        visited[min_vertex] = True
        for edge, weight in adjlist[min_vertex]:
            if distance[edge] > distance[min_vertex] + weight:
                distance[edge] = distance[min_vertex] + weight
                heapq.heapreplace(heap,(distance[edge],edge))

    return distance

ret = dijkstra(k)
for i in range(1,V+1):
    if ret[i] == sys.maxsize:
        print('INF')
    else:
        print(ret[i])

