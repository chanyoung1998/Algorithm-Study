import sys
def dfs(row,col,cnt,color):

    if col >= n:
        row+= 1
        if col % 2 == 0:
            col = 1
        else:
            col = 0

    if row >= n:
        ans[color] = max(ans[color],cnt)
        return

    if board[row][col] == 1 and diagonal_up[col+row] == 0 and diagonal_down[n+(col-row)] == 0:
        diagonal_up[col + row] = diagonal_down[n + (col - row)] =1
        dfs(row,col+2,cnt+1,color)
        diagonal_up[col + row] = diagonal_down[n + (col - row)] = 0

    dfs(row,col+2,cnt,color)
    return




n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
diagonal_up = [0 for _ in range(2 * n)]
diagonal_down = [0 for _ in range(2 * n)]
ans = [0,0]
dfs(0,0,0,0)
dfs(0,1,0,1)
print(ans[0]+ans[1])
