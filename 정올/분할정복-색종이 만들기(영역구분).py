import sys
#백준1780번 문제도 숙제로 내주기
n = int(sys.stdin.readline().rstrip())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

white = 0
blue = 0


def sol(a,b,width):
    global white,blue

    if width == 1:
        if board[a][b] == 0:
            white += 1
        else:
            blue += 1
        return


    cnt = 0
    for i in range(a,a+width//2):
        for j in range(b,b+width//2):
            cnt += board[i][j]

    if cnt == (width//2) ** 2:
        blue += 1
    elif cnt == 0:
        white += 1
    else:
        sol(a+width//4,b+width//4,width//2)

    cnt = 0
    for i in range(a-width//2,a):
        for j in range(b,b+width//2):
            cnt += board[i][j]
    if cnt == (width//2) ** 2:
        blue += 1
    elif cnt == 0:
        white += 1
    else:
        sol(a-width//4,b+width//4,width//2)

    cnt = 0
    for i in range(a - width // 2, a):
        for j in range(b-width//2,b):
            cnt += board[i][j]
    if cnt == (width // 2) ** 2:
        blue += 1
    elif cnt == 0:
        white += 1
    else:
        sol(a - width // 4, b - width // 4, width // 2)

    cnt = 0
    for i in range(a, a+width//2):
        for j in range(b-width//2, b):
            cnt += board[i][j]
    if cnt == (width // 2) ** 2:
        blue += 1
    elif cnt == 0:
        white += 1
    else:
        sol(a + width // 4, b - width // 4, width // 2)


sum_ = 0
for board_ in board:
    sum_ += sum(board_)
if sum_ == 0:
    white += 1
elif sum_ == n ** 2:
    blue += 1
else:
    sol(n//2,n//2,n)

print(white,blue,sep='\n')


'''
import sys
input = sys.stdin.readline
len = int(input())
paper = [[] for i in range(len)]
for i in range(len):
    paper[i] = list(map(int, input().split()))
# 2X2 정사각형에서 네 칸이 모두 같으면 True, 한 칸이라도 다르면 False
def equal(sum):
    for i in range(1, 4):
        if sum[i] != sum[i-1]:
            return False
    if sum[0] == [1, 0] or sum[0] == [0,1]:
        return True
    else:
        return False

#
def get_count(x, y, len):
    if len == 1:
        return [1, 0] if paper[x][y] == 1 else [0,1]
    sum = [0 for _ in range(4)]
    x_list = [x, x + len//2, x, x + len//2]
    y_list = [y, y, y + len//2, y + len//2]

    for i in range(4):
        sum[i] = get_count(x_list[i], y_list[i], len//2)

    if equal(sum): # 2X2 정사각형에서 네 칸의 색종이가 모두 같은 색이 경우, 2X2 정사각형을 하나의 색종이로 본다
        return sum[0]
    else:
        blue_count, white_count = 0, 0
        for i in range(4):
            blue_count += sum[i][0]
            white_count += sum[i][1]
        return [blue_count, white_count]

blue_count, white_count = get_count(0, 0, len)
print(white_count)
print(blue_count)
'''