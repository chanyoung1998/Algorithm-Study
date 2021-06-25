import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    vectors = []
    for _ in range(n):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        vectors.append((x,y))
