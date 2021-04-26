'''
내용:백준 알고리즘 단계별 풀기 유니온 파인드 4195 친구 네트워크
날짜:21년4월26일
사용 언어:파이썬
'''

import sys
sys.setrecursionlimit(10**6)
def find(x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    parent[x] += parent[y]
    parent[y] = x

t = int(sys.stdin.readline())
for _ in range(t):
    f = int(sys.stdin.readline())
    network = dict()
    count = 0
    parent = dict()
    for i in range(f):
        friend1,friend2 = sys.stdin.readline().rstrip().split()
        if friend1 not in network:
            network[friend1] = count
            parent[count] = -1
            count += 1
        if friend2 not in network:
            network[friend2] = count
            parent[count] = -1
            count += 1

        a = network[friend1]
        b = network[friend2]

        union(a,b)
        print(abs(parent[find(a)]))

