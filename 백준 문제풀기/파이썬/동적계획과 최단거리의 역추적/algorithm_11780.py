'''
내용:백준 알고리즘 단계별 풀기 동적계획과 최단거리의 역추적 11780 플로이드2
날짜:21년5월 16일
사용 언어:파이썬
'''
import sys
INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dp = [[INF for _ in range(n)] for _ in range(n)]
path = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    if dp[a-1][b-1] > c:
        dp[a-1][b-1] = c
for i in range(n):
    dp[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                path[i][j] = path[i][k] + [k] + path[k][j]
for ret in dp:
    for i in ret:
        if i == INF:
            print(0,end=' ')
        else:
            print(i,end=' ')
    print()

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or dp[i][j] == INF:
            print(0)
        else:
            ret = [i+1]
            for x in path[i][j]:
                ret.append(x+1)
            ret.append(j+1)
            print(len(ret),end=' ')
            print(*ret)


