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
    islands_x = list(map(int,input().rstrip().split()))
    islands_y = list(map(int, input().rstrip().split()))
    E = float(input())
    parent = [i for i in range(n)]
    edge = []
    for i in range(n):
        for j in range(i+1,n):
            c = ((islands_x[i]-islands_x[j]) ** 2 + (islands_y[i]-islands_y[j]) ** 2) * E
            # costs[j][i], costs[i][j] = c, c
            edge.append((i,j,c))

    edge.sort(key=lambda x:(x[2]))

    ret = 0
    for i,j,c in edge:

        if find(i) != find(j):
            union(i,j)
            ret += c

    print("#{} {}".format(t+1,round(ret)))

