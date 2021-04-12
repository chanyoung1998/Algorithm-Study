'''
내용:백준 알고리즘 단계별 풀기 최단 경로 11404번 플로이드
날짜:21년4월 12일
사용 언어:파이썬
'''

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dest = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    if dest[a][b] != sys.maxsize and dest[a][b] > c:
        dest[a][b] = c
    elif dest[a][b] == sys.maxsize:
        dest[a][b] = c


for i in range(1,n+1): # 거쳐가는 노드
    for j in range(1,n+1): # 출발 노드
        for k in range(1,n+1): # 도착 노드
            if dest[j][k] > dest[j][i] + dest[i][k]:
                dest[j][k] = dest[j][i] + dest[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print(0,end=' ')
            continue

        if dest[i][j] == sys.maxsize:
            print(0,end=' ')
        else:
            print(dest[i][j],end=' ')

    print()


