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

    if x > y:
        parent[y] = parent[x]
    else:
        parent[x] = parent[y]


T = int(input())
for t in range(T):
    n = int(input())
    parent = [i for i in range(n)]
    m = int(input())
    edge = []
    for i in range(m):
        edge.append(tuple(map(int,input().rstrip().split())))

    edge.sort(key=lambda x:(x[2]))

    ret = 0
    for i,j,c in edge:
        i = i-1
        j = j-1
        if find(i) != find(j):
            union(i,j)
            ret += c

    print("#{} {}".format(t+1,ret))

