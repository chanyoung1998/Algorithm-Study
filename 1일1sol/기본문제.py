import sys

maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(10)]
x,y = 1,1
while True:
    if maps[x][y] == 0:
        maps[x][y] = 9

    if maps[x][y] == 2:
        maps[x][y] = 9
        break

    if y + 1 < 10:
        if maps[x][y+1] == 0:
            y = y+1
        elif maps[x][y+1] == 1:
            if x +1 < 9:
                x = x+1
            else:
                break

for _ in maps:
    print(*_)

