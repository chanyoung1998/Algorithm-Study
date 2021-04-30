
import sys

v, e = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(v+1)]
edges = []
parent = [i for i in range(v+1)]
for _ in range(e):
    a, b, c =  map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append((b,c))
    adjlist[b].append((a,c))
    edges.append((a,b,c))

edges.sort(key=lambda x : x[2])

def find(a):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):

    a = find(a)
    b = find(b)

    if a == b:
        return

    if b > a:
        parent[b] = a
    else:
        parent[a] = b

    return

def isSameParent(a,b):

    a = find(a)
    b = find(b)

    if a == b:
        return True
    else:
        return False


count = 0
mst = 0
for a,b,c in edges:
    if count == v-1:
        break
    if isSameParent(a,b):
        continue
    else:
        union(a,b)
        count += 1
        mst += c
print(mst)