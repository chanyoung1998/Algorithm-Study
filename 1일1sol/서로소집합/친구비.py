import sys

n,m,k = map(int,sys.stdin.readline().rstrip().split())
friendcost = [0] + list(map(int,sys.stdin.readline().rstrip().split()))
parent = [i for i in range(n+1)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):

    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    union(a,b)
for i in range(1,n+1):
    find(i)

min_cost = [sys.maxsize for _ in range(n+1)]
for i in range(1,n+1):
    min_cost[parent[i]] = min(min_cost[parent[i]],friendcost[i])

ret = 0
for i in range(1,n+1):
    if min_cost[i] != sys.maxsize:
        ret += min_cost[i]


if ret > k:
    print("Oh no")
else:
    print(ret)
