import sys

board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(19)]

def check(a,b):
    cnt = 1
    for i in range(1,19):
        if b + i < 19:
            if board[a][b] == board[a][b+i]:
                cnt += 1
            else:
                break

    if cnt == 5:
        if board[a][b] != board[a][b-1]:
            return 1
    cnt = 1
    for i in range(1,19):
        if a +i < 19:
            if board[a][b] == board[a+i][b]:
                cnt += 1
            else:
                break

    if cnt == 5:
        if board[a][b] != board[a-1][b]:
            return 1

    cnt = 1
    for i in range(1,19):
        if a + i < 19 and b + i < 19:
            if board[a][b] == board[a+i][b+i]:
                cnt += 1
            else:
                break

    if cnt == 5:
        if board[a][b] != board[a - 1][b-1]:
            return 1

    cnt = 1
    for i in range(1, 19):
        if a + i < 19 and b - i >= 0:
            if board[a][b] == board[a + i][b - i]:
                cnt += 1
            else:
                break

    if cnt == 5:
        if board[a][b] != board[a-1][b+1]:
            return 2


    return 0


for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            k = check(i,j)
            if k == 1:
                print(board[i][j])
                print(i+1,j+1)
                exit(1)
            elif k == 2:
                print(board[i][j])
                print(i+1 + 4,j+1 -4)
                exit(1)

print(0)