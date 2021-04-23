'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 1167 트리의 지름
날짜:21년4월 22일
사용 언어:파이썬
'''
import sys

def dfs(vertex,length):
    global max
    global max_index
    if max < length:
        max = length
        max_index = vertex
    visited[vertex] = True

    for v, cost in adjlist[vertex]:
        if not visited[v]:
            dfs(v, length + cost)
    return

n = int(sys.stdin.readline())
adjlist = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    vertex = temp[0]
    i = 1
    while temp[i] != -1:
        adjlist[vertex].append((temp[i],temp[i+1]))
        i += 2

max = 0
max_index = -1
dfs(1,0)

visited = [False for _ in range(n+1)]
max = 0
dfs(max_index,0)
print(max)
