'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 1967 트리의 지름
날짜:21년4월 22일
사용 언어:파이썬
'''
import sys
sys.setrecursionlimit(100000)
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
for _ in range(n-1):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    adjlist[temp[0]].append((temp[1],temp[2]))
    adjlist[temp[1]].append((temp[0], temp[2]))
max = 0
max_index = 0
dfs(1,0)
visited = [False for _ in range(n+1)]
max = 0
dfs(max_index,0)
print(max)
