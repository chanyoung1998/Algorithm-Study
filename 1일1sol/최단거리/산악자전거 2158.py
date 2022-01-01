import sys
import heapq

def dijkstra(v):
    time = [[sys.maxsize for _ in range(c)] for _ in range(r)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    pq = []
    #  최단 거리,현재 속력, 행위치,열위치
    heapq.heappush(pq, (0, v, 0, 0))
    time[0][0] = 0

    while pq:
        cur_time, cur_v, x, y = heapq.heappop(pq)
        if time[x][y] < cur_time:
            continue
        for i in range(4):
            p = x + dx[i]
            q = y + dy[i]
            if 0 <= p < r and 0 <= q < c:
                next_v = cur_v * 2 ** (mountain[x][y] - mountain[p][q])
                n_time_spent = cur_time + 1 / cur_v
                if time[p][q] > n_time_spent:
                    time[p][q] = n_time_spent
                    heapq.heappush(pq, (n_time_spent,next_v, p, q))
    return time[r-1][c-1]


v,r,c = map(int,sys.stdin.readline().rstrip().split())
mountain = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(r)]
print(round(dijkstra(v),2))

