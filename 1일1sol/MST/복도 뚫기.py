import sys
def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: return
    if x < y:
        parent[x] = y
    else:
        parent[y] = x

    return



test_case = int(sys.stdin.readline())

for _ in range(test_case):
    w = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    circle = []
    edge = []
    parent = [i for i in range(n+2)]
    for _ in range(n):
        circle.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

    for i in range(n):
        dist = circle[i][0] - circle[i][2]
        edge.append((i,n,dist)) # 왼쪽벽-i
        dist = w - circle[i][0]-circle[i][2]
        edge.append((i,n+1,dist)) #i-오른벽

        for j in range(i+1,n):
            dist = ((circle[i][0]-circle[j][0]) ** 2 + (circle[i][1]-circle[j][1])**2) **0.5 - circle[i][2] - circle[j][2]
            edge.append((i,j,dist))

    edge.sort(key=lambda x:x[2])

    for a,b,e in edge:
        a = find(a)
        b = find(b)

        if a == b:
            continue

        union(a,b)
        if find(n) == find(n+1):
            if e <= 0:
                print(0)
                break
            else:
                print(round(e/2,6))
                break

    if n == 0:
        print(round(w/2,6))


