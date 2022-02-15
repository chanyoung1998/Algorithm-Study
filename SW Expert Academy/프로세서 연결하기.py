
def sol(index,board,cnt,length):
    global max_cnt,min_length
    if index == len(core):
        if max_cnt < cnt:
            max_cnt = cnt
            min_length = length
        elif max_cnt ==cnt:
            min_length = min(min_length,length)
        return

    x = core[index][0]
    y = core[index][1]

    flag = True
    for i in range(x+1,n):
        if board[i][y] != 0:
            flag = False
            break

    if flag:
        for i in range(x+1,n):
            board[i][y] = 1
        sol(index+1,board,cnt+1,length+n-x-1)
        for i in range(x+1,n):
            board[i][y] = 0
##########################################################
    flag = True
    for i in range(x-1,-1,-1):
        if board[i][y] != 0:
            flag = False
            break

    if flag:
        for i in range(x-1,-1,-1):
            board[i][y] = 1
        sol(index + 1, board, cnt + 1, length + x)
        for i in range(x-1,-1,-1):
            board[i][y] = 0

##########################################################
    flag = True
    for i in range(y+1,n):
        if board[x][i] != 0:
            flag = False
            break

    if flag:
        for i in range(y+1,n):
            board[x][i] = 1
        sol(index + 1, board, cnt + 1, length + n-y-1)
        for i in range(y+1,n):
            board[x][i] = 0
##########################################################
    flag = True
    for i in range(y -1,-1,-1):
        if board[x][i] != 0:
            flag = False
            break

    if flag:
        for i in range(y -1,-1,-1):
            board[x][i] = 1
        sol(index + 1, board, cnt + 1, length +y)
        for i in range(y -1,-1,-1):
            board[x][i] = 0

    sol(index+1,board,cnt,length) # core연결 안 한 경우

    return





T = int(input())
for t in range(T):
    n = int(input())
    Board = [list(map(int,input().rstrip().split())) for _ in range(n)]
    core = []
    max_cnt = 0
    min_length = 999999
    for i in range(n):
        for j in range(n):
            if Board[i][j] == 1:
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    continue
                core.append((i,j))
    if len(core) == 0:
        min_length = 0
    else:
        sol(0,Board,0,0)
    print('#{} {}'.format(t+1,min_length))