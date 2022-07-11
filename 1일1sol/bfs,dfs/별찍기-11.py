n = int(input())

arr = [[' ' for _ in range(2*n)] for _ in range(n)]

def triangle(n,row,col):

    if n == 3:
        arr[row][col] = '*'
        arr[row+1][col-1] ='*'
        arr[row+1][col+1] = '*'
        arr[row +2][col-2] = '*'
        arr[row + 2][col -1] = '*'
        arr[row + 2][col] = '*'
        arr[row + 2][col + 1] = '*'
        arr[row + 2][col + 2] = '*'
        return


    triangle(n//2, row,col)
    triangle(n//2,row+n//2,col-n//2)
    triangle(n // 2, row + n // 2, col + n // 2)

triangle(n,0,n-1)

for i in range(n):
    for j in range(2*n-1):
        print(arr[i][j],end='')
    print()