import sys

n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().rstrip().split())
a,b = a-1,b-1
b = 2**n-1 - b
maps = [[0 for _ in range(2**n)] for _ in range(2**n)]
maps[b][a] = -1

def check(l,x,y):
    for i in range(x,x+l):
        for j in range(y,y+l):
            if maps[i][j] != 0:
                return False

    return True

count = 0

def sol(l,x,y):

    global count
    count += 1
    if l == 2:
        if maps[x][y] == 0:
            maps[x][y] = count
        if maps[x+1][y] == 0:
            maps[x+1][y] = count
        if maps[x][y+1] == 0:
            maps[x][y+1] = count
        if maps[x+1][y+1] == 0:
            maps[x+1][y+1] = count

        return

    if check(l//2,x,y):
        maps[x-1+l//2][y-1+l//2] = count
    if check(l//2,x,y+l//2):
        maps[x-1+l//2][y+l//2] = count
    if check(l//2,x+l//2,y):
        maps[x+l//2][y-1+l//2] = count
    if check(l//2,x+l//2,y+l//2):
        maps[x+l//2][y+l//2] = count


    sol(l // 2, x, y)
    sol(l // 2, x, y + l // 2)
    sol(l // 2, x + l // 2, y)
    sol(l // 2, x + l // 2, y + l // 2)

sol(2**n,0,0)
for array in maps:
    print(*array)
