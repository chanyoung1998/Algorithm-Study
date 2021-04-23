'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 11725 트리의 부모 찾기
날짜:21년4월 22일
사용 언어:파이썬
'''


import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
adjlist = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
parent[1] = 0   # root노드의 부모는 없다

for _ in range(n-1):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()
    for k in adjlist[x]:
        if parent[k] == -1:
            parent[k] = x
            queue.append(k)
for i in range(2,n+1):
    print(parent[i])
