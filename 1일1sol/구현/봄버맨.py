import sys

r, c, n = map(int, sys.stdin.readline().strip().split(' '))

maps = [list(sys.stdin.readline().strip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for w in range(r):
    for z in range(c):
        if maps[w][z] == 'O':
            maps[w][z] = 0

if n % 2 == 0:
    n = 2
elif n == 1:
    n = 1
elif n % 4 == 1: #,5,9,13
    n = 5
elif n % 4 == 3:
    n = 7


for i in range(1, n + 1):
    if i % 2 == 0:
        for w in range(r):
            for z in range(c):
                if maps[w][z] == '.':
                    maps[w][z] = i
    else:
        for w in range(r):
            for z in range(c):
                if maps[w][z] != '.' and maps[w][z] + 3 == i:
                    maps[w][z] = '.'
                    for d in range(4):
                        if 0 <= w + dx[d] < r and 0 <= z + dy[d] < c and (maps[w + dx[d]][z + dy[d]] != '.' and maps[w + dx[d]][z + dy[d]] + 3 != i):
                            maps[w + dx[d]][z + dy[d]] = '.'

for ma in maps:
    for m in ma:
        if m == '.':
            print(m,end='')
        else:
            print('O',end='')

    print()



