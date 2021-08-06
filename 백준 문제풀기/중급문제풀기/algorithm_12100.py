import sys
import copy
# deep copy 해야하는 것 잊지 말기
n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

def up(board):
    temp = copy.deepcopy(board)
    #i열 부터 검사
    for i in range(n):
        j = 0
        while j < n:
            if temp[j][i] == 0:
                onlyZero = True
                for k in range(j,n-1):
                    if temp[k+1][i] != 0:
                        onlyZero = False
                    temp[k][i] = temp[k+1][i]
                temp[n-1][i] = 0
                if onlyZero:
                    j += 1
                continue

            target = temp[j][i]
            for k in range(j+1,n):
                if temp[k][i] == target:
                    temp[j][i] *= 2
                    temp[k][i] = 0
                    break
                elif temp[k][i] == 0:
                    continue
                else:
                    break
            j += 1

    return temp

def down(board):
    temp = copy.deepcopy(board)
    # i열 부터 검사
    for i in range(n):
        j = n-1
        while j >= 0:
            if temp[j][i] == 0:
                onlyZero = True
                for k in range(j,0,-1):
                    if temp[k - 1][i] != 0:
                        onlyZero = False
                    temp[k][i] = temp[k - 1][i]
                temp[0][i] = 0
                if onlyZero:
                    j -= 1
                continue

            target = temp[j][i]
            for k in range(j-1,-1,-1):
                if temp[k][i] == target:
                    temp[j][i] *= 2
                    temp[k][i] = 0
                    break
                elif temp[k][i] == 0:
                    continue
                else:
                    break
            j -= 1

    return temp

def left(board):
    temp = copy.deepcopy(board)
    #i행 부터 검사
    for i in range(n):
        j = 0
        while j < n:
            if temp[i][j] == 0:
                onlyZero = True
                for k in range(j,n-1):
                    if temp[i][k+1] != 0:
                        onlyZero = False
                    temp[i][k] = temp[i][k+1]
                temp[i][n-1] = 0
                if onlyZero:
                    j += 1
                continue

            target = temp[i][j]
            for k in range(j+1,n):
                if temp[i][k] == target:
                    temp[i][j] *= 2
                    temp[i][k] = 0
                    break
                elif temp[i][k] == 0:
                    continue
                else:
                    break
            j += 1

    return temp

def right(board):
    # i행 부터 검사
    temp = copy.deepcopy(board)
    for i in range(n):
        j = n - 1
        while j >= 0:
            if temp[i][j] == 0:
                onlyZero = True
                for k in range(j, 0, -1):
                    if temp[i][k-1] != 0:
                        onlyZero = False
                    temp[i][k] = temp[i][k-1]
                temp[i][0] = 0
                if onlyZero:
                    j -= 1
                continue

            target = temp[i][j]
            for k in range(j - 1, -1, -1):
                if temp[i][k] == target:
                    temp[i][j] *= 2
                    temp[i][k] = 0
                    break
                elif temp[i][k] == 0:
                    continue
                else:
                    break
            j -= 1

    return temp

ret = 0
def sol(count,board):
    global ret



    if count == 5:
        for i in range(n):
            ret = max(ret,max(board[i]))
        return

    for i in range(4):
       # print(board)
        if i == 0:
            new_board = up(board)
            sol(count+1,new_board)
        elif i == 1:
            new_board = down(board)
            sol(count+1, new_board)
        elif i == 2:
            new_board = left(board)
            sol(count+1, new_board)
        elif i == 3:
            new_board = right(board)
            sol(count+1, new_board)

    return

sol(0,board)
print(ret)