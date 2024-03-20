'''
24 03 19
중량제한
1939
골3
이분탐색
'''
import sys
from collections import deque

# sys.setrecursionlimit(100000)

def checkBfs(currentFactory, target):

    dq = deque()
    dq.append(currentFactory)

    visit[currentFactory] = True

    while dq:
        factory = dq.popleft()

        if factory == factoryB:
            return True

        for nextFactory, weight in bridges[factory]:
            if weight >= target and not visit[nextFactory]:
                dq.append(nextFactory)
                visit[nextFactory] = True

    return False
def check(currentFactory, target):

    if currentFactory == factoryB:
        return True

    visit[currentFactory] = True

    for nextFactory, weight in bridges[currentFactory]:
        if weight >= target and not visit[nextFactory]:
            if check(nextFactory,target):
                return True

    return False


N,M = map(int,sys.stdin.readline().strip().split(' '))

bridges = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().strip().split(' '))
    bridges[a].append((b,c))
    bridges[b].append((a,c))

factoryA, factoryB = map(int,sys.stdin.readline().strip().split(' '))

low = 0
high = 1000000001

while low + 1 < high:
    mid = (low+high) // 2
    visit = [False for _ in range(N+1)]
    if checkBfs(factoryA,  mid):
        low = mid
    else:
        high = mid

print(low)