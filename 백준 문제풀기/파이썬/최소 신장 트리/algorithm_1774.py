'''
내용:백준 알고리즘 단계별 풀기 최소 신장 트리 1774 우주신과의 교감
날짜:21년4월30일
사용 언어:파이썬
'''
import sys
from itertools import combinations


def distance(a,b):
    dis = ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5
    return dis

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


n, m = map(int,sys.stdin.readline().rstrip().split())
points = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
already_connected = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(m)]
edges = []
parent = [i for i in range(n)]

for a,b in list(combinations(range(n),2)):
    c = distance(points[a],points[b])
    edges.append((a,b,c))

edges.sort(key=lambda x: x[2])
count = 0
mst = 0
for a,b in already_connected:
    if not isSameParent(a-1,b-1):
        union(a-1,b-1)
        count += 1

for a,b,c in edges:
    if isSameParent(a,b):
        continue
    else:
        union(a,b)
        count += 1
        mst += c
    if count == n-1:
        break

print(format(mst,".2f"))
