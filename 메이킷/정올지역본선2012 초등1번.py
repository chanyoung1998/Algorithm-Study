import sys

a,b = map(int,sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline().rstrip())

while c > 0:
    if b + c >= 60:
        c -= 60-b
        b = 0
        a = (a+1) % 24
    else:
        b = b + c
        c = 0

print(a,b)
