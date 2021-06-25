import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    prev_ranking = list(map(lambda x:x-1,map(int,sys.stdin.readline().rstrip().split())))
    m = int(sys.stdin.readline())
    changed_ranking = []
    graph = [[False] * n for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            graph[prev_ranking[i]][prev_ranking[j]] = True
            indegree[prev_ranking[j]] += 1

    for _ in range(m):
        a, b = map(lambda x:x-1,map(int,sys.stdin.readline().rstrip().split()))
        changed_ranking.append((a,b))
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[b] += 1
            indegree[a] -= 1


    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    cycle = False
    certain = True
    result = []
    for i in range(n):
        if len(queue) >= 2:
            certain = False
            break
        if len(queue) == 0:
            cycle = True
            break

        x = queue.popleft()
        result.append(x+1)
        for i in range(n):
            if graph[x][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

    if not certain:
        print("?")
    elif cycle:
        print("IMPOSSIBLE")
    else:
        print(*result)