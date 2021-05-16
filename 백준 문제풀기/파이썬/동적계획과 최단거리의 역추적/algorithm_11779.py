'''
내용:백준 알고리즘 단계별 풀기 동적계획과 최단거리의 역추적 11779 최소비용 구하기2
날짜:21년5월 14일
사용 언어:파이썬
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adjlist = [[] for _ in range(n+1)]
INF = sys.maxsize
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append((b, c))

dp = [INF for _ in range(n+1)]
visited = [False for _ in range(n+1)]
path = [-1 for _ in range(n+1)]
start,end = map(int,sys.stdin.readline().rstrip().split())
dp[start] = 0

for _ in range(n):
    min = INF
    x = None
    for i in range(1,n+1):
        if not visited[i] and min > dp[i]:
            min = dp[i]
            x = i
    if x == None:
        break
    visited[x] = True
    for a,w in adjlist[x]:
        if dp[a] > dp[x] + w:
            dp[a] = dp[x] + w
            path[a] = x

if n == 1:
    print(0)
    print(1)
    print(start)
else:
    city = path[end]
    ret = []
    ret.append(end)
    while True:
        if city == start:
            break
        ret.append(city)
        city = path[city]
    ret.append(start)
    print(dp[end])
    print(len(ret))
    print(*ret[::-1])