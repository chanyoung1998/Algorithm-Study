import sys
from collections import deque
n, m = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n)]
indegree = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a-1].append(b-1)
    indegree[b-1] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

    return result

for i in topology_sort():
    print(i+1,end=' ')