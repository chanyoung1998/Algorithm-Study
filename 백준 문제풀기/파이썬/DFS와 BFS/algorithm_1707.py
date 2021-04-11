'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 1707번 이분 그래프
날짜:21년4월 11일
사용 언어:파이썬
'''

import sys
from collections import deque


def check_Yes_No():
    for i in range(v + 1):
        for j in adjlist[i]:
            if check[i] == check[j]:
                print('NO')
                return
    print('YES')
    return

k = int(sys.stdin.readline())
for i in range(k):
    v, e = map(int,sys.stdin.readline().split())
    adjlist = [[] for _ in range(v+1)]
    check = [1 for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    flag = True
    queue = deque()

    for _ in range(e):
        v1, v2 = map(int,sys.stdin.readline().split())
        adjlist[v1].append(v2)
        adjlist[v2].append(v1)

    for i in range(v+1):
        if not visited[i]:
            queue.append(i)

        while queue:
            x = queue.popleft()
            visited[x] = True
            for i in adjlist[x]:
                if not visited[i]:
                    queue.append(i)
                    check[i] = -1 * check[x]
                    continue
                if check[i] == check[x]:
                    flag = False
                    break

    if flag:
        print('YES')
    else:
        print('NO')


