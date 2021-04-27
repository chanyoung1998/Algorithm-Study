import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n ,m = map(int,sys.stdin.readline().rstrip().split())
    for _ in range(m):
        a, b = map(int,sys.stdin.readline().rstrip().split())
    print(n-1)

