'''
24 03 07
우주 탐사선
17182
플로이드 와샬, 비트 마스킹
'''

import sys

n, K = map(int, sys.stdin.readline().strip().split(' '))
adjmatrix = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
minCost = sys.maxsize

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adjmatrix[i][k] + adjmatrix[k][j] < adjmatrix[i][j]:
                adjmatrix[i][j] = adjmatrix[i][k] + adjmatrix[k][j]


def dfs(cur, visit, cost):
    global minCost

    if visit == (1 << n) - 1:
        minCost = min(minCost, cost)
        return cost

    for i in range(n):

        if visit & (1 << i):
            continue

        dfs(i, visit | (1 << i), adjmatrix[cur][i] + cost)

dfs(K,1 << K , 0)

print(minCost)