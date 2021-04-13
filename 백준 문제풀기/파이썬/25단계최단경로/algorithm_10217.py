'''
내용:백준 알고리즘 단계별 풀기 최단 경로 10217번 KCM Travel
날짜:21년4월 13일
사용 언어:파이썬
'''
'''
시간 초과 난다 ( 다른 언어로는 통과ㅣ)
import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    n, m, k = map(int,sys.stdin.readline().rstrip().split())
    adjlist = [[] for _ in range(n+1)]
    dp = [[sys.maxsize for _ in range(m+1)] for _ in range(n+1)]
    queue = deque()
    queue.append((1,0,0))

    for _ in range(k):
        u, v, c, d = map(int,sys.stdin.readline().rstrip().split())
        adjlist[u].append((v,c,d))

    while queue:
        cur,ccost,cdis = queue.popleft()

        for v,c,d in adjlist[cur]:
            ncost = ccost + c
            ndis = cdis + d
            if ncost > m or dp[v][ncost] <= ndis :
                continue
            dp[v][ncost] = ndis
            queue.append((v,ncost,ndis))

    ret = min(dp[n][:m+1])
    if ret == sys.maxsize:
        print('Poor KCM')
    else:
        print(ret)

'''

import sys

T = int(input())
INF = sys.maxsize

for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())  # 공항수,지원비용,티켓정보수
    ticket = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())  # 출발,도착,비용,소요시간
        ticket[u].append([v, c, d])

    DP = [[INF for _ in range(M + 1)] for _ in range(N + 1)]  # 열:비용 행:n까지갈때
    DP[1][0] = 0  # 1->1로 갔을때 비용은0 시간도 0

    for c in range(M + 1):
        for d in range(1, N + 1):
            if DP[d][c] == INF: continue  # c의 비용으로 d에 도착하는 경우가 없다면
            t = DP[d][c]  # c의 비용으로 d에 도착햇을때의 소요시간
            for dv, dc, dd in ticket[d]:  # d에서 출발하는 모든경우
                if dc + c > M:  # 비용이 초과될경우 넘어간다
                    continue
                DP[dv][dc + c] = min(DP[dv][dc + c], t + dd)  # 이전에 저장된값과 비교하여 작다면 갱신해준다

    result = min(DP[N])  # N에 도착할때 최소소요시간

    if result == INF:
        print('Poor KCM')
    else:
        print(result)
