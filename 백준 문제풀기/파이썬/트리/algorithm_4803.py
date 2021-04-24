'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 4803 트리
날짜:21년4월 24일
사용 언어:파이썬
'''
import sys
from collections import deque

def bfs(start):

    queue = deque()
    queue.append(start)
    edge = 0
    vertex = 0
    while queue:
        x = queue.popleft()
        if visited[x]:
            continue
        vertex += 1
        visited[x] = True
        for y in adjlist[x]:
            queue.append(y)
            edge += 1

    if edge//2 == vertex - 1:
        return True
    else:
        return False

test_case = 0
while True:
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    if temp[0] == 0 and temp[1] == 0:
        break

    n, m = temp[0],temp[1]
    test_case += 1
    adjlist = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        adjlist[a].append(b)
        adjlist[b].append(a)
    count = 0
    for i in range(1,n+1):
        if not visited[i]:
            if bfs(i):
                count += 1
    if count == 0:
        print('Case {}: No trees.'.format(test_case))
    elif count == 1:
        print('Case {}: There is one tree.'.format(test_case))
    else:
        print('Case {}: A forest of {} trees.'.format(test_case,count))
