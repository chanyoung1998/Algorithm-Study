'''
내용:백준 알고리즘 단계별 풀기 최소 신장 트리 1197
날짜:21년4월28일
사용 언어:파이썬
'''

import sys
import heapq
INF = 2147483647
v, e = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(v+1)]
cost = [2147483647 for _ in range(v+1)]
cost[1] = 0
isInMST = [False for _ in range(v+1)]
E = [None for _ in range(v+1)]
mst = 0
for _ in range(e):
    a, b, c =  map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append((b,c))
    adjlist[b].append((a,c))

heap = []

for i in range(1,v+1):
    heapq.heappush(heap,(cost[i],i))

while heap:
    cost_, v = heapq.heappop(heap)

    if isInMST[v]:
        continue

    isInMST[v] = True

    if E[v] != None:
        mst += cost_

    for w, c in adjlist[v]:
        if not isInMST[w] and c < cost[w]:
            heap.remove((cost[w],w))
            cost[w] = c
            E[w] = v
            heapq.heappush(heap,(cost[w],w))

print(mst)