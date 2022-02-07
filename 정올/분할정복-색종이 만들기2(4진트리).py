'''
import sys

n = int(sys.stdin.readline().rstrip())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
ret = ''

def sol(x,y,size):
    global ret
    temp = board[x][y]
    flag = True
    for i in range(x,x+size):
        if not flag:
            break

        for j in range(y,y+size):
            if temp != board[i][j]:
                flag = False
                break

    if flag:

        if temp == 0:
            ret += '0'
        elif temp == 1:
            ret += '1'
    else:
        ret += 'X'
        sol(x,y,size//2)
        sol(x,y+size//2,size//2)
        sol(x+size//2,y,size//2)
        sol(x+size//2,y+size//2,size//2)

sol(0,0,n)
print(ret)'''


def check(row, col, n):
    global ret

    v = paper[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if v != paper[i][j]:
                print('X',end='')
                for k in [0,1]:
                    for l in [0,1]:
                        check(row + k * n // 2, col + l * n // 2, n // 2)
                return

    if v == 0:
        print('0',end='')
    elif v == 1:
        print('1',end='')

    return

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
check(0, 0, N)
