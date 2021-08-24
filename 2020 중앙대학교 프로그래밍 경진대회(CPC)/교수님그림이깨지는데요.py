import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
bitmap = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

new_bitmap = [[0] * (n*k) for _ in range(n*k)]
for i in range(n*k):
    for j in range(n*k):
        new_bitmap[i][j] = bitmap[i // k][j // k]

for new in new_bitmap:
    print(*new)