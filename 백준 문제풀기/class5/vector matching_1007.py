import sys
from itertools import combinations
def destination(x, y, p, q):
    return ((x - p) ** 2 + (y - q) ** 2) ** 0.5

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    vectors = []
    check = [False for _ in range(n)]
    for _ in range(n):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        vectors.append((x,y))

    combination = list(combinations(range(n),n//2))
    result = sys.maxsize
    for comb in combination[:len(combination)//2]:
        sum_x = 0
        sum_y = 0
        for i in range(n):
            if i in comb:
                sum_x += vectors[i][0]
                sum_y += vectors[i][1]

            else:
                sum_x -= vectors[i][0]
                sum_y -= vectors[i][1]

        result = min(result,(sum_x**2 + sum_y**2)**0.5)

    print(result)
