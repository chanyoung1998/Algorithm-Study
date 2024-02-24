import sys
from collections import deque
#최단거리 탐색
#넓이우선탐색
#bfs
n,k = map(int,sys.stdin.readline().rstrip().split())
coins = list(sys.stdin.readline().rstrip())
dp = [[-1 for _ in range(n+1)]for _ in range(n+1)]
h = 0
t = 0
for i in range(n):
    if coins[i] == 'H':
        h += 1
    else:
        t += 1

dp[h][t] = 0
queue = deque()
queue.append((h,t))
while queue:
    cur_h,cur_t = queue.popleft()
    for i in range(k+1):
        if cur_h >= i and cur_t >= k - i:
            next_h = cur_h - i + (k-i)
            next_t = n - next_h
            if dp[next_h][next_t] == -1:
                dp[next_h][next_t] = dp[cur_h][cur_t] + 1
                queue.append((next_h,next_t))

if dp[0][n] == -1:
    print(-1)
else:
    print(dp[0][n])
