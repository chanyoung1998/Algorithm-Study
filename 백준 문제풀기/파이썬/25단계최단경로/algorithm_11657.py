'''
내용:백준 알고리즘 단계별 풀기 최단 경로 11657번 타임머신
날짜:21년4월 12일
사용 언어:파이썬
'''
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]
distance = [sys.maxsize for _ in range(n+1)]
distance[1] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adjlist[a].append((b,c))

for _ in range(n-1):
    for i in range(1,n+1):
        for dest, wei in adjlist[i]:
            if distance[i] != sys.maxsize and distance[dest] > distance[i] + wei:
                distance[dest] = distance[i] + wei

temp = distance.copy()
for i in range(1, n + 1):
    for dest, wei in adjlist[i]:
        if temp[i] != sys.maxsize and temp[dest] > temp[i] + wei:
            temp[dest] = temp[i] + wei

if temp.__eq__(distance):
    for i in range(2,n+1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)
