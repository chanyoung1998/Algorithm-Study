'''
닭싸움 팀 정하기
1765
골2
유니온 파인드, 서로소 집합
'''
import sys

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):

    x = find(x)
    y = find(y)

    if x > y:
        x,y = y,x

    parent[y] = x


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n+1)]
enemy = [[] for _ in range(n+1)]
for _ in range(m):
    relation, p, q = sys.stdin.readline().strip().split(' ')
    p = int(p)
    q = int(q)
    if relation == 'E':
        enemy[p].append(q)
        enemy[q].append(p)
    else:
        union(p,q)
# 1 - 4
# 1 - 2
for i in range(1,n+1):
    for e1 in enemy[i]:
        for e2 in enemy[e1]:
            union(i,e2)

retSet = set()
for i in range(1,n+1):
    retSet.add(find(i))

print(len(retSet))