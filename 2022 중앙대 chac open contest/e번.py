import sys

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):

    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n,m = map(int,sys.stdin.readline().rstrip().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    union(a,b)


arrays = list(map(int,sys.stdin.readline().rstrip().split()))
ret = 0
for i in range(len(arrays) - 1):
    if find(arrays[i]) == find(arrays[i+1]):
        continue
    ret += 1

print(ret)