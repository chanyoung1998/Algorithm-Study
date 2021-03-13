'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 1260번
날짜:21년3월 13일
사용 언어:파이썬
'''
import sys
from collections import deque


def dfs(vertex):
    visted[vertex] = True
    print(vertex,end=' ')

    for post in adjlist[vertex]:
        if not visted[post]:
            dfs(post)

    return


def bfs(v):
    que.append(v)
    visted[v] = True
    print(v,end=' ')
    while len(que) != 0:
        pop_vertex = que.popleft()
        for post in adjlist[pop_vertex]:
            if not visted[post]:
                que.append(post)
                visted[post] = True
                print(post,end=' ')
    return


n, m, v = map(int, sys.stdin.readline().split())
edges = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]

adjlist = [[] for _ in range(n+1)]

for edge in edges:
    adjlist[edge[0]].append(edge[1])
    adjlist[edge[1]].append(edge[0])
for adj in adjlist:
    adj.sort(key = lambda x: x)


visted = [False for _ in range(n+1)]
dfs(v)

que = deque()
que.append(v)
visted = [False for _ in range(n+1)]
print()
bfs(v)
