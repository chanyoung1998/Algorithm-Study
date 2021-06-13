import sys

n = int(sys.stdin.readline())
point = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]


s = 0
for i in range(1,n-1):
    x1 = point[0][0]
    y1 = point[0][1]

    x2 = point[i][0]
    y2 = point[i][1]

    x3 = point[i+1][0]
    y3 = point[i+1][1]

    s += ((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))

print(abs(round(s/2,1)))
