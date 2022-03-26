n = int(input())
array = [[-1 for _ in range(2*n-1)] for _ in range(2*n-1)]
x = 0
y = n-1
dir = 0
dx =[1,1,-1,-1]
dy=[-1,1,1,-1]
alpha = 65
side_size = n
for i in range(n):
    x = i
    y = n-1

    for j in range(4):
        for k in range(1,side_size):
            array[x][y] = (alpha)
            alpha += 1
            if alpha+1 >90: alpha = 65
            x = x + dx[j]
            y = y + dy[j]

    side_size -= 1


array[n-1][n-1] = (alpha)
for i in range(2*n-1):
    print(array[i])