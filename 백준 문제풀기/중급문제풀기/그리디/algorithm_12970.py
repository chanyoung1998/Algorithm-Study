import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

s = ['B' for _ in range(n)]

temp = -1
for i in range(n):
    if k <= i * (n-i):
        temp = i
        break


if temp == -1:
    print(-1)
else:

    for i in range(temp-1):
        s[i] = 'A'
    s[-1] = 'A'

    count = (temp-1)*(n-temp)

    for i in range(n-1,temp-2,-1):
        if count == k:
            print(*s,sep='')
            exit(0)

        s[i] = 'B'
        s[i-1] ='A'
        count += 1


    print(-1)
