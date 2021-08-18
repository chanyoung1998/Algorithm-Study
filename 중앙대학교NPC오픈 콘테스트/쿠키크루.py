import sys
from collections import deque
from itertools import permutations
n = int(sys.stdin.readline())
topping_map = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

home = tuple()
end = tuple()
assassin = []
healer = []
mage = []
tanker = []

for i in range(n):
    for j in range(n):
        if topping_map[i][j] == 'J':
            assassin.append((i,j))
        elif topping_map[i][j] == 'C':
            healer.append((i,j))
        elif topping_map[i][j] == 'B':
            mage.append((i,j))
        elif topping_map[i][j] == 'W':
            tanker.append((i, j))
        elif topping_map[i][j] == 'H':
            home = (i,j)
        elif topping_map[i][j] == '#':
            end = (i,j)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

'''def sol(start,targets):

    targets.append(end)
    visit = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append(start)
    visit[start[0]][start[1]] = 1
    count = 0
    target = 0
    while queue:
        x,y = queue.popleft()

        if x == targets[target][0] and y == targets[target][1]:
            target += 1
            count += visit[x][y]
            if target == 4:
                break
            else:
                visit = [[0 for _ in range(n)] for _ in range(n)]
                queue = deque()
                visit[x][y] = 1

        for dir in range(4):
            p = x + dx[dir]
            q = y + dy[dir]

            if 0 <= p < n and 0 <= q < n and visit[p][q] == 0:
                visit[p][q] = visit[x][y] + 1
                queue.append((p,q))


    return count
'''
def sol(home,targets):
    count = 0
    targets.append(end)
    a,b = home
    for x,y in  targets:
        count += abs(a-x) + abs(b-y)
        a,b = x,y

    return count


field = ''
min_time = sys.maxsize
for target in permutations(assassin):
    target = list(target)
    time = sol(home,target)
    if time < min_time:
        field = 'Assassin'
        min_time = time

for target in permutations(healer):
    target = list(target)
    time = sol(home,target)
    if time < min_time:
        field = 'Healer'
        min_time = time

for target in permutations(mage):
    target = list(target)
    time = sol(home,target)
    if time < min_time:
        field = 'Mage'
        min_time = time

for target in permutations(tanker):
    target = list(target)
    time = sol(home,target)
    if time < min_time:
        field = 'Tanker'
        break

print(field)