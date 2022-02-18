# https://hoho325.tistory.com/111

from heapq import heappop,heappush

T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
INF = 99999999999999
for t in range(1,T+1):
    n = int(input())
    maps = [list(map(int,input().rstrip())) for _ in range(n)]
    heap = []
    # (cost,x,y)
    heappush(heap,(0,0,0))
    visit = [[INF for _ in range(n)] for _ in range(n)]
    while heap:
        cost,x,y = heappop(heap)
        if x == n-1 and y == n-1:
            print('#{} {}'.format(t,cost))
            break
        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]

            if 0 <= p < n and 0 <= q < n:
                if visit[p][q] == INF:
                    visit[p][q] = cost + maps[p][q]
                    heappush(heap,(cost+maps[p][q],p,q))

