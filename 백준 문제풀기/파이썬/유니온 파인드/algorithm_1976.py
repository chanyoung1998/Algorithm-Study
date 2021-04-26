'''
내용:백준 알고리즘 단계별 풀기 유니온 파인드 1976 여행 가자
날짜:21년4월25일
사용 언어:파이썬
'''
import sys

def find(x):
    if parent[x] == x:
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


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [i for i in range(n+1)]
routes = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
plan = list(map(int,sys.stdin.readline().rstrip().split()))
for i,route in enumerate(routes):
    for j,Islinked in enumerate(route):
        if Islinked == 1:
            union(i+1,j+1)
ret = []
for city in plan:
    ret.append(find(city))

if ret.count(find(plan[0])) == len(plan):
    print('YES')
else:
    print('NO')

