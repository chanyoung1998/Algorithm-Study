import sys
import math
from collections import deque
n = int(sys.stdin.readline())
adjlist = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
height = [0 for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append((b,c))
    adjlist[b].append((a,c))


def bfs(root):
    queue = deque()
    queue.append(root)
    parent[root] = 0
    while queue:
        pop_data = queue.popleft()
        for i,w in adjlist[pop_data]:
            if parent[i] == -1:
                parent[i] = pop_data
                height[i] = height[pop_data] + 1
                queue.append(i)

    return
bfs(1)
# print('parent',parent)
# print('height',height)

max_height = max(height)
x = math.ceil(math.log2(max_height))
dp = [[0 for _ in range(x+1)] for _ in range(n+1)]
min_dp = [[0 for _ in range(x+1)] for _ in range(n+1)]
max_dp = [[0 for _ in range(x+1)] for _ in range(n+1)]

def build_dp():
    for i in range(1,n+1):
        dp[i][0] = parent[i]
        for j,w in adjlist[parent[i]]:
            if j == i:
                min_dp[i][0] = w
                max_dp[i][0] = w
                break

    for k in range(1,x+1):
        for i in range(1,n+1):
            dp[i][k] = dp[dp[i][k-1]][k-1]
            min_dp[i][k] = min(min_dp[i][k - 1], min_dp[dp[i][k - 1]][k - 1])
            max_dp[i][k] = max(max_dp[i][k - 1], max_dp[dp[i][k - 1]][k - 1])

    return

build_dp()


k = int(sys.stdin.readline())
for _ in range(k):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    min_weight = sys.maxsize
    max_weight = -sys.maxsize
    # 같은 높이로 맞혀주는 과정
    if height[a] > height[b]:
        diff = height[a]-height[b]
        w = math.ceil(math.log2(diff))
        while w >=0:
            if diff >= 2**w:
                min_weight = min(min_weight,min_dp[a][w])
                max_weight = max(max_weight,max_dp[a][w])
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
                min_weight = min(min_weight, min_dp[b][w])
                max_weight = max(max_weight, max_dp[b][w])
                b = dp[b][w]
                diff -= 2 ** w
                w -= 1
            else:
                w -= 1

    if a == b:
        print(min_weight,max_weight)

    else:
        for h in range(x,-1,-1):
            if dp[a][h] != dp[b][h]:
                min_weight = min(min_weight, min_dp[a][h],min_dp[b][h])
                max_weight = max(max_weight, max_dp[a][h],max_dp[b][h])
                a = dp[a][h]
                b = dp[b][h]
        print(min(min_weight,min_dp[a][0],min_dp[b][0]),max(max_weight,max_dp[a][0],max_dp[b][0]))
