'''
내용:백준 알고리즘 단계별 풀기 최단 경로 1956번 운동
날짜:21년4월 13일
사용 언어:파이썬
'''

import sys

v,e = map(int,sys.stdin.readline().rstrip().split())
dest = [[sys.maxsize for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    dest[a][b] = c

for i in range(1,v+1): # 거쳐가는 노드
    for j in range(1,v+1): # 출발 노드
        for k in range(1,v+1): # 도착 노드
            if dest[j][k] > dest[j][i] + dest[i][k]:
                dest[j][k] = dest[j][i] + dest[i][k]

min_cycle = sys.maxsize
for i in range(1,v+1):
    for j in range(i+1,v+1):
        if dest[i][j] == sys.maxsize or dest[j][i] == sys.maxsize:
            continue
        min_cycle = min(dest[i][j] + dest[j][i],min_cycle)

print(min_cycle if min_cycle != sys.maxsize else -1)
