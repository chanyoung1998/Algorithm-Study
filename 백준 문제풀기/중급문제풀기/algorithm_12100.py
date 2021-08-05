import sys
import copy
n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

def up(board):
    #i열 부터 검사
    for i in range(n):
        j = 0
        while j < n:
            if board[j][i] == 0:
                onlyZero = True
                for k in range(j,n-1):
                    if board[k+1][i] != 0:
                        onlyZero = False
                    board[k][i] = board[k+1][i]
                board[n-1][i] = 0
                if onlyZero:
                    j += 1
                continue

            target = board[j][i]
            for k in range(j+1,n):
                if board[k][i] == target:
                    board[j][i] *= 2
                    board[k][i] = 0
                    break
                elif board[k][i] == 0:
                    continue
                else:
                    break
            j += 1

    return board

def down(board):

    # i열 부터 검사
    for i in range(n):
        j = n-1
        while j >= 0:
            if board[j][i] == 0:
                onlyZero = True
                for k in range(j,0,-1):
                    if board[k - 1][i] != 0:
                        onlyZero = False
                    board[k][i] = board[k - 1][i]
                board[0][i] = 0
                if onlyZero:
                    j -= 1
                continue

            target = board[j][i]
            for k in range(j-1,-1,-1):
                if board[k][i] == target:
                    board[j][i] *= 2
                    board[k][i] = 0
                    break
                elif board[k][i] == 0:
                    continue
                else:
                    break
            j -= 1

    return board

def left(board):

    #i행 부터 검사
    for i in range(n):
        j = 0
        while j < n:
            if board[i][j] == 0:
                onlyZero = True
                for k in range(j,n-1):
                    if board[i][k+1] != 0:
                        onlyZero = False
                    board[i][k] = board[i][k+1]
                board[i][n-1] = 0
                if onlyZero:
                    j += 1
                continue

            target = board[i][j]
            for k in range(j+1,n):
                if board[i][k] == target:
                    board[i][j] *= 2
                    board[i][k] = 0
                    break
                elif board[i][k] == 0:
                    continue
                else:
                    break
            j += 1

    return board

def right(board):
    # i행 부터 검사

    for i in range(n):
        j = n - 1
        while j >= 0:
            if board[i][j] == 0:
                onlyZero = True
                for k in range(j, 0, -1):
                    if board[i][k-1] != 0:
                        onlyZero = False
                    board[i][k] = board[i][k-1]
                board[i][0] = 0
                if onlyZero:
                    j -= 1
                continue

            target = board[i][j]
            for k in range(j - 1, -1, -1):
                if board[i][k] == target:
                    board[i][j] *= 2
                    board[i][k] = 0
                    break
                elif board[i][k] == 0:
                    continue
                else:
                    break
            j -= 1

    return board

ret = 0
def sol(count,board):
    global ret

    temp = copy.deepcopy(board)

    if count == 5:
        for i in range(n):
            ret = max(ret,max(board[i]))
        return

    for i in range(4):
       # print(board)
        if i == 0:
            new_board = up(temp)
            sol(count+1,new_board)
        elif i == 1:
            new_board = down(temp)
            sol(count+1, new_board)
        elif i == 2:
            new_board = left(temp)
            sol(count+1, new_board)
        elif i == 3:
            new_board = right(temp)
            sol(count+1, new_board)

    return

sol(0,board)
print(ret)