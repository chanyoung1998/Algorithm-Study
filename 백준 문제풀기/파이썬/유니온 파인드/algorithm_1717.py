'''
내용:백준 알고리즘 단계별 풀기 유니온 파인드 1717 집합의 표현
날짜:21년4월25일
사용 언어:파이썬
'''

import sys
sys.setrecursionlimit(10**5)
n,m = map(int,sys.stdin.readline().rstrip().split())
parent = [-1  for _ in range(n+1)]
#-1이라는 것은 자기 자신이 부모라는 것

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def isSameParent(a,b):
    x = find(a)
    y = find(b)

    if x == y:
        return True
    else:
        return False

for _ in range(m):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    if temp[0] == 0:
        union(temp[1],temp[2])
    elif temp[0] == 1:
        flag = isSameParent(temp[1],temp[2])
        if flag:
            print('YES')
        else:
            print('NO')
