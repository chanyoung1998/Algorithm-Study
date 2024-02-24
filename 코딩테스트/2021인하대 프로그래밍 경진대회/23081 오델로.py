import sys
n = int(sys.stdin.readline())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
possible = []

def check(i,j):
    ret = 0

#가로
    white = 0
    black = False
    nothing = False
    for x in range(i+1,n):
        if maps[x][j] == 'W':
            white += 1
        elif maps[x][j] == 'B':
            black = True
            break
        elif maps[x][j] == '.':
            nothing = True
            break

    if black:
        ret += white

    white = 0
    black = False
    nothing = False
    for x in range(i-1,-1,-1):
        if maps[x][j] == 'W':
            white += 1
        elif maps[x][j] == 'B':
            black = True
            break
        elif maps[x][j] == '.':
            nothing = True
            break

    if black:
        ret += white

#세로
    white = 0
    black = False
    nothing = False
    for y in range(j+1,n,1):
        if maps[i][y] == 'W':
            white += 1
        elif maps[i][y] == 'B':
            black = True
            break
        elif maps[i][y] == '.':
            nothing = True
            break

    if black:
        ret += white

    white = 0
    black = False
    nothing = False
    for y in range(j-1,-1,-1):
        if maps[i][y] == 'W':
            white += 1
        elif maps[i][y] == 'B':
            black = True
            break
        elif maps[i][y] == '.':
            nothing = True
            break

    if black:
        ret += white

#대각선
    white = 0
    black = False
    nothing = False
    for x in range(1,n):
        if 0 <= i + x < n and 0 <= j + x < n:
            if maps[i+x][j+x] == 'W':
                white += 1
            elif maps[i+x][j+x] == 'B':
                black = True
                break
            elif maps[i+x][j+x] == '.':
                nothing = True
                break
        else:
            break

    if black:
        ret += white

    white = 0
    black = False
    nothing = False
    for x in range(1, n):
        if 0 <= i + x < n and 0 <= j - x < n:
            if maps[i + x][j - x] == 'W':
                white += 1
            elif maps[i + x][j - x] == 'B':
                black = True
                break
            elif maps[i + x][j - x] == '.':
                nothing = True
                break
        else:
            break
    if black:
        ret += white

    white = 0
    black = False
    nothing = False
    for x in range(1, n):
        if 0 <= i - x < n and 0 <= j + x < n:
            if maps[i - x][j + x] == 'W':
                white += 1
            elif maps[i - x][j + x] == 'B':
                black = True
                break
            elif maps[i - x][j + x] == '.':
                nothing = True
                break
        else:
            break
    if black:
        ret += white

    white = 0
    black = False
    nothing = False
    for x in range(1, n):
        if 0 <= i - x < n and 0 <= j - x < n:
            if maps[i - x][j - x] == 'W':
                white += 1
            elif maps[i - x][j - x] == 'B':
                black = True
                break
            elif maps[i - x][j - x] == '.':
                nothing = True
                break
        else:
            break
    if black:
        ret += white

    return ret



ret = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == '.':
            ret.append((i,j,check(i,j)))

ret.sort(key=lambda x:(-x[2],x[0],x[1]))

if ret[0][2] == 0:
    print('PASS')
else:
    print(ret[0][1],ret[0][0])
    print(ret[0][2])

