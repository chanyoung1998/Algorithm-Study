import sys
from collections import deque
INF = sys.maxsize
m,n = map(int,sys.stdin.readline().rstrip().split())
route_x = [[] for _ in range(n+1)] #수평 방향 루트
route_y = [[] for _ in range(m+1)] #수직 방향 루트
for _ in range(int(sys.stdin.readline().rstrip())):
    b,x,y,w,z = map(int,sys.stdin.readline().rstrip().split())
    if x == w:
        if z < y:
            y,z =z,y
        route_y[x].append([b,y,z,INF])
    else:
        if w < x:
            x,w = w,x
        route_x[y].append([b,x,w,INF])

s_x,s_y,d_x,d_y = map(int,sys.stdin.readline().rstrip().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

dq = deque()
dq.append((s_x,s_x,s_y,s_y,0))

ret = INF
while dq:

    from_x,to_x,from_y,to_y,cur_dist = dq.popleft()

    if from_x <= d_x <= to_x and from_y <= d_y <= to_y:
        ret = min(ret,cur_dist)

    for y in range(from_y,to_y+1):
        for i in range(len(route_x[y])):
            _, from_p, to_p, next_dist = route_x[y][i]
            if (from_p <= from_x <= to_p or from_p <= to_x <= to_p) and next_dist > cur_dist + 1:
               route_x[y][i] = [_,from_p,to_p,cur_dist+1]
               dq.append((from_p,to_p,y,y,cur_dist+1))


    for x in range(from_x,to_x+1):
        for i in range(len(route_y[x])):
            _, from_q, to_q, next_dist = route_y[x][i]
            if (from_q <= from_y <= to_q or from_q <= to_y <= to_q) and next_dist > cur_dist + 1:
                route_y[x][i] = [_,from_q,to_q,cur_dist+1]
                dq.append((x,x,from_q,to_q,cur_dist+1))



print(ret)