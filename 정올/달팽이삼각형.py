n = int(input())

dx = [1,0,-1]
dy = [1,-1,0]
array = [[-1 for _ in range(n)] for _ in range(n)]
num = 0
x,y =0,0
dir = 0
while True:

    array[x][y] = num


    next_x = x + dx[dir]
    next_y = y + dy[dir]

    if not (0 <= next_x < n and 0<= next_y < n):
        dir = (dir+1)%3
        next_x = x + dx[dir]
        next_y = y + dy[dir]
    elif array[next_x][next_y] != -1:
        dir = (dir + 1) % 3
        next_x = x + dx[dir]
        next_y = y + dy[dir]

    if array[next_x][next_y] != -1:
        break

    x = next_x
    y = next_y
    num = (num + 1) % 10

for i in range(n):
    for j in range(i+1):
        print(array[i][j],end=' ')
    print()






