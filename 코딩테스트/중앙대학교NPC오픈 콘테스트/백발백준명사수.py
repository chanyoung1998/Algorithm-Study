import sys

x1,y1,r1 = map(int,sys.stdin.readline().rstrip().split())
x2,y2,r2 = map(int,sys.stdin.readline().rstrip().split())

if ((x1-x2)**2 + (y1-y2)**2)**0.5 >= r1 + r2:
    print('NO')
else:
    print("YES")