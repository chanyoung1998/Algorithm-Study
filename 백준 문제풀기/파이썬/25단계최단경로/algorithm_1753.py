'''
내용:백준 알고리즘 단계별 풀기 최단 경로 1753 최단경로
날짜:21년4월 11일
사용 언어:파이썬
'''

import sys
import heapq


def dijkstra(start):
    distance = [sys.maxsize for _ in range(V+1)]
    distance[start] = 0
    for i in range(V-2):
        min_vertex = getSmallIndex(distance)
        visited[min_vertex] = True
        for edge, weight in adjlist[min_vertex]:
            if distance[edge] > distance[min_vertex] + weight:
                distance[edge] = distance[min_vertex] + weight
    return distance

# 선형시간을 탐색함 -> O(n^2)
def getSmallIndex(distance):
    min = sys.maxsize
    ret = -1
    for i in range(1,V+1):
        if min > distance[i] and not visited[i]:
            min = distance[i]
            ret = i
    return ret

# 방문하지 않은 노드 중 dist가 가장 작은 노드를 찾을 때 heap을 사용하여 찾는 것 -> O(nlogn)
def dijkstra2(start):
    distance = [sys.maxsize for _ in range(V+1)]
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


V, E = map(int,sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())
adjlist = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))

ret = dijkstra2(k)
for i in range(1,V+1):
    if ret[i] == sys.maxsize:
        print('INF')
    else:
        print(ret[i])

