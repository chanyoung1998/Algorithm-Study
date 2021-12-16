import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
edges = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    edges.append((a,b,c))

edges.sort(key=lambda x:x[2])

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

cost = 0
for (a,b,c) in edges:
    a_parent = find(a)
    b_parent = find(b)

    if a_parent != b_parent:
        union(a,b)
        cost += c

print(cost)