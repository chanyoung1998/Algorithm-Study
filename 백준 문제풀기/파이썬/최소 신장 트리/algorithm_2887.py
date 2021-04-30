'''
내용:백준 알고리즘 단계별 풀기 최소 신장 트리 2887 해성 터널
날짜:21년4월30일
사용 언어:파이썬
'''

import sys


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
points = [[i] + list(map(int,sys.stdin.readline().rstrip().split())) for i in range(n)]
distances = []
parent = [i for i in range(n)]

for i in range(3):
    points.sort(key=lambda x: x[i+1])
    for j in range(n-1):
        a = points[j]
        b = points[j+1]
        dis = abs(a[i+1] - b[i+1])
        distances.append((a[0],b[0],dis))

distances.sort(key=lambda x: x[2])
count = 0
mst = 0
for a,b,c in distances:
    if count == n-1:
        break
    if isSameParent(a,b):
        continue
    else:
        union(a,b)
        count += 1
        mst += c

print(mst)