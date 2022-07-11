import sys

n, m = map(int, sys.stdin.readline().split())
edge = []
parent = [i for i in range(n + 1)]

for _ in range(m+1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edge.append((a, b, c))


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 피로도가 가장 작은 길

edge.sort(key=lambda x: -x[2])
cnt = 0
min_ret = 0
for a, b, c in edge:

    if find(a) != find(b):
        union(a, b)
        min_ret += 1 if c == 0 else 0
        cnt += 1

# 피로도가 가장 큰 길
parent = [i for i in range(n + 1)]
edge.sort(key=lambda x: x[2])
cnt = 0
max_ret = 0
for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        max_ret += 1 if c == 0 else 0
        cnt += 1



print(max_ret**2-min_ret**2)