import sys

#dfs 와 비트마스킹 기법도 사용가능
n, m = map(int,sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
maximum = 0
def sol(i,j,string):
    global maximum
    if board[i][j] in string:
        maximum = max(maximum,len(string))
        return
    string += board[i][j]
    for dir in range(4):
        p = i + dx[dir]
        q = j + dy[dir]
        if 0 <= p < n and 0 <= q < m:
            sol(p,q,string)

    return

sol(0,0,'')
print(maximum)