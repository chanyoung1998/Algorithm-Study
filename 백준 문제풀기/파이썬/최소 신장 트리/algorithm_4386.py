'''
내용:백준 알고리즘 단계별 풀기 최소 신장 트리 4386 별자리 만들기
날짜:21년4월30일
사용 언어:파이썬
'''

import sys
from itertools import combinations


def distance(a,b):
    dis = ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5
    return dis.__round__(2)

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


n = int(sys.stdin.readline().rstrip())
points = [tuple(map(float,sys.stdin.readline().rstrip().split())) for _ in range(n)]
edges = []
parent = [i for i in range(n)]

for a,b in list(combinations(range(n),2)):
    c = distance(points[a],points[b])
    edges.append((a,b,c))

edges.sort(key= lambda x:x[2])
count = 0
mst = 0
for a,b,c in edges:
    if count == n-1:
        break
    if isSameParent(a,b):
        continue
    else:
        union(a,b)
        count += 1
        mst += c
print(mst)

