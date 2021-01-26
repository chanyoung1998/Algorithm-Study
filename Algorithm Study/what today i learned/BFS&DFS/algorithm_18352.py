'''
내용:백준 1835 특정 거리의 도시 찾기
날짜:21년1월26일
사용 언어:파이썬
'''
from collections import deque
import sys

n,m,k,x = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
city = [0 for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)


def bfs(x):
    queue = deque([x])

    visited[x] = True

    while queue:
        v = queue.popleft()
        for b in graph[v]:
            if visited[b] == False:
                queue.append(b)
                visited[b] =True
                city[b] += city[v]+1


bfs(x)
count = 0
for i in range(n+1):
   if city[i] == k :
       print(i)
       count += 1

if count ==0:
    print(-1)
