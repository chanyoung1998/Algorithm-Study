from collections import deque


def check(x,y):
    ret = 0
    for dir in range(8):
        p = x + dx[dir]
        q = y + dy[dir]
        if 0 <= p < n and 0 <= q < n:
            if maps[p][q] == '*':
                ret += 1

    return ret

def click(x,y):
    global ans
    dq = deque()
    dq.append((x,y))
    count[x][y] = -1
    # 먼저 주위에 지뢰가 없는 것들 부터 누른다
    while dq:
        cur_x,cur_y = dq.popleft()

        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0<= next_x < n and 0<= next_y < n:
                if maps[next_x][next_y] == '*' or count[next_x][next_y] == -1:
                    continue

                if count[next_x][next_y] == 0:
                    dq.append((next_x,next_y))

                count[next_x][next_y] = -1








dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

T = int(input())
for t in range(T):

    n = int(input())
    maps = [list(input().rstrip()) for _ in range(n)]
    count = [[0 for _ in range(n)] for _ in range(n)]
    ret = 0

    for i in range(n):
        for j in range(n):
            if maps[i][j] == '.':
                count[i][j] = check(i,j)

    # 지뢰가 주위에 없는 것부터 먼저 눌러주기
    for i in range(n):
        for j in range(n):
            if maps[i][j] == '.' and count[i][j] == 0:
                click(i,j)
                ret += 1

    #지뢰가 아닌 것 중 아직 방문 처리 안 된 것들 눌러주기
    for i in range(n):
        for j in range(n):
            if maps[i][j] == '.' and count[i][j] > 0:
                ret += 1


    print('#{} {}'.format(t+1,ret))
