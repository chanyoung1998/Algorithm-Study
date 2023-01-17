import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

coord = [tuple(map(lambda x: int(x) , sys.stdin.readline().split())) for _ in range(m)]
preFixSum_Dim2 = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        preFixSum_Dim2[i][j] = (preFixSum_Dim2[i][j - 1] if j - 1 >= 0 else 0) + board[i-1][j-1]

for i in range(1,n+1):
    for j in range(1,n+1):
        preFixSum_Dim2[i][j] += preFixSum_Dim2[i - 1][j] if i - 1 >= 0 else 0

for i in range(m):
    x1, y1, x2, y2 = coord[i]
    print(preFixSum_Dim2[x2][y2] + preFixSum_Dim2[x1-1][y1-1] - preFixSum_Dim2[x2][y1-1] - preFixSum_Dim2[x1-1][y2])