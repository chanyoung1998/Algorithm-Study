import sys

n,q = map(int,sys.stdin.readline().rstrip().split())
logs= []
quest = []
parent = [i for i in range(n)]
for i in range(n):
    x1,x2,h = map(int,sys.stdin.readline().rstrip().split())
    logs.append((x1,x2,i))
for _ in range(q):
    quest.append(tuple(map(int,sys.stdin.readline().rstrip().split())))



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
    else:
        if x > y:
            x, y = y, x
        parent[y] = x
    return

logs.sort(key=lambda x:x[0])
st = logs[0][0]
en = logs[0][1]
for i in range(1,n):
    if en < logs[i][0]:
        st = logs[i][0]
        en = logs[i][1]
        continue
    else:
        union(logs[i][2],logs[i-1][2])
        en = max(en,logs[i][1])


for a,b in quest:
    if find(a-1) == find(b-1):
        print(1)
    else:
        print(0)

