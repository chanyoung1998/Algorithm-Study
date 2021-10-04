import sys
'''
"스패닝 트리에서 파란색 간선의 최소 개수를 Bmin,
최대 개수를 Bmax라 할 때, Bmin <= k <= Bmax라면
 그러한 스패닝 트리는 반드시 존재한다."
'''

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
        x, y = y, x

    parent[y] = x
    return


def MinST(n,edges):

    edges.sort(key=lambda x: x[2])
    count = 0
    ret = 0
    for i in range(len(edges)):
        if count == n-1:
            break
        u, v, w = edges[i][0], edges[i][1], edges[i][2]
        if find(u) == find(v):
            continue
        else:
            union(u, v)
            count += 1
            ret += w

    return ret


def MaxST(n, edges):
    edges.sort(key=lambda x: -x[2])
    count = 0
    ret = 0
    for i in range(len(edges)):
        if count == n - 1:
            break
        u, v, w = edges[i][0], edges[i][1], edges[i][2]
        if find(u) == find(v):
            continue
        else:
            union(u, v)
            count += 1
            ret += w

    return ret


while True:
    n,m,k = map(int,sys.stdin.readline().rstrip().split())
    edges = []
    if n == 0 and m == 0 and k == 0:
        break
    for _ in range(m):
        c,u,v = sys.stdin.readline().rstrip().split()
        u,v = int(u),int(v)
        if c == 'B':
            edges.append((u, v, 1))
        else:
            edges.append((u, v, 0))

    parent = [i for i in range(n + 1)]
    a = MinST(n,edges)
    parent = [i for i in range(n + 1)]
    b = MaxST(n,edges)
    if a <= k <= b:
        print(1)
    else:
        print(0)