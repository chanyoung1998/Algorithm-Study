'''
내용:백준 알고리즘 단계별 풀기 유니온 파인드 20040 사이클 게임
날짜:21년4월26일
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

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return

def isSameParent(a,b):

    x = find(a)
    y = find(b)

    if x == y:
        return True
    else:
        return False


n, m = map(int,sys.stdin.readline().rstrip().split())
parent = [i for i in range(n)]
first = True
time = 0
for i in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())

    if first and isSameParent(a,b):
        time = i
        first = False

    union(a,b)
if time == 0:
    print(0)
else:
    print(time+1)