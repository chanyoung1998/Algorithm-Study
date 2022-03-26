import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
basic_array = [[0 for _ in range(n)] for _ in range(n)]
basic_array[0][0] = 1
for i in range(1,n):
    for j in range(i+1):
        # (i-1,j),(i-1,j-1)
        basic_array[i][j] = basic_array[i-1][j] + (basic_array[i-1][j-1] if j -1 >=0 else 0)



if m == 1:
    for i in range(n):
        for j in range(i+1):
            print(basic_array[i][j],end=' ')
    print()
elif m == 2:
    for i in range(n-1,-1,-1):
        for j in range(n-1-i):
            print(" ",end='')
        for j in range(i,-1,-1):
            print(basic_array[i][j],end=' ')
        print()
elif m == 3:
    cnt = 0
    for i in range(n-1,-1,-1):
        for j in range(n-1,n-1-cnt-1,-1):
            # print(j,i)
            print(basic_array[j][i],end=' ')
        print()
        cnt += 1