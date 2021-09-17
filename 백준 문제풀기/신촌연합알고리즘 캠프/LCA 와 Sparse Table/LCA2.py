import sys
import math
from collections import deque


n = int(sys.stdin.readline())
adjlist = [[] for _ in range(n+1)]
height = [-1 for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append(b)
    adjlist[b].append(a)


def bfs(root):
    queue = deque()
    queue.append(root)
    height[root] = 0
    parent[root] = 0
    while queue:
        x = queue.popleft()
        h = height[x]

        for y in adjlist[x]:
            if height[y] == -1:
                queue.append(y)
                height[y] = h + 1
                parent[y] = x
    return
bfs(1)
# print('height',height)
# print('parent',parent)

max_h = max(height)
x = math.ceil(math.log2(max_h))
dp = [[0 for _ in range(x+1)] for _ in range(n+1)]

def build_dp():
    for i in range(1,n+1):
        dp[i][0] = parent[i]

    for k in range(1,x+1):
        for i in range(1,n+1):
            dp[i][k] = dp[dp[i][k-1]][k-1]

    return

build_dp()
# print('dp',dp)
m = int(sys.stdin.readline())
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())

    if height[a] > height[b]:
        diff = height[a]-height[b]
        w = math.ceil(math.log2(diff))
        while w >=0:
            if diff >= 2**w:
                a = dp[a][w]
                diff -= 2**w
                w -= 1
            else:
                w -= 1
    elif height[a] < height[b]:
        diff = height[b] - height[a]
        w = math.ceil(math.log2(diff))
        while w >= 0:
            if diff >= 2 ** w:
                b = dp[b][w]
                diff -= 2 ** w
                w -= 1
            else:
                w -= 1

    if a == b:
        print(a)
    else:
        for h in range(x,-1,-1):
            if dp[a][h] != dp[b][h]:
                a = dp[a][h]
                b = dp[b][h]
        print(dp[a][0])




