import sys
from collections import deque

n,m,h = map(int,sys.stdin.readline().rstrip().split())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
home = tuple()
mint = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home = (i, j)
        elif maps[i][j] == 2:
            mint.append((i, j))


#bfs는 시간초과 발생 n,m,h 가 만약 10 10 10이면 모든 경우를 탐색하게된다.
'''def sol(home_x,home_y):
    queue = deque()
    queue.append((home_x,home_y,m,0,0))
    max_count = 0
    while queue:
        x,y,cur_hp,visited,count = queue.popleft()
        if max_count == len(mint):
            break
        for i in range(len(mint)):
            mint_x = mint[i][0]
            mint_y = mint[i][1]
            dist = abs(mint_x - x) + abs(mint_y-y)
            if dist <= cur_hp and not (visited & (1 << i)):
                queue.append((mint_x,mint_y,cur_hp-dist + h,visited | (1 << i), count + 1))

        if abs(home_x-x) + abs(home_y-y) <= cur_hp:
            max_count = max(max_count,count)

    return max_count'''


max_count = 0
def sol2(cur_x,cur_y,cur_hp,visited,count):
    global max_count
    if max_count == len(mint):
        return

    if abs(home[0] - cur_x) + abs(home[1] - cur_y) <= cur_hp:
        max_count = max(max_count, count)

    for i in range(len(mint)):
        mint_x = mint[i][0]
        mint_y = mint[i][1]
        dist = abs(mint_x - cur_x) + abs(mint_y - cur_y)
        if dist <= cur_hp and not (visited & (1 << i)):
            sol2(mint_x, mint_y, cur_hp - dist + h, visited | (1 << i), count + 1)


sol2(home[0],home[1],m,0,0)
print(max_count)



