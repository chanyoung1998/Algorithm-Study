import sys

def find(a):
    if parent[a] == a or a == -1:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

    return True


n,m,k = map(int,sys.stdin.readline().rstrip().split())
power = list(map(int,sys.stdin.readline().rstrip().split()))
edge = []
parent = [i for i in range(n+1)]
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    edge.append((u,v,w))
edge.sort(key= lambda x : x[2])

for p in power:
    parent[p] = -1


ret = 0
for u,v,w in edge:

    if union(u,v):
        ret += w

print(ret)