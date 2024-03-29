import sys

n, m, l, k = map(int, sys.stdin.readline().strip().split(' '))
coordinate = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(k)]

coordinate.sort(key=lambda x : (x[0],x[1]))

candidate = set()
for i in range(k):
    for j in range(k):
        candidate.add((coordinate[i][0],coordinate[i][1]))
        candidate.add((coordinate[i][0],coordinate[j][1]))
        candidate.add((coordinate[j][0],coordinate[i][1]))


ret = k
for rangeX1,rangeY1 in candidate:

    rangeX2 = rangeX1 + l
    rangeY2 = rangeY1 + l

    notIncluded = 0
    for j in range(k):
        x, y = coordinate[j]

        if not ((rangeX1 <= x <= rangeX2) and (rangeY1 <= y <= rangeY2)):
            notIncluded += 1

    ret = min(ret, notIncluded)

print(ret)
