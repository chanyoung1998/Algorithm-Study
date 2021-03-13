'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 2606번 바이러스
날짜:21년3월 13일
사용 언어:파이썬
'''
import sys


def dfs(vertex):
    global count
    visited[vertex] = True

    for post in adjlist[vertex]:
        if not visited[post]:
            dfs(post)
            count += 1

    return

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = [tuple(map(int,sys.stdin.readline().split())) for _ in range(m)]
adjlist = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0
for edge in edges:
    adjlist[edge[0]].append(edge[1])
    adjlist[edge[1]].append(edge[0])

dfs(1)
print(count)
