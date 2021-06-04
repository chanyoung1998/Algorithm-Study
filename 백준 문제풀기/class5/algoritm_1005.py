import sys
from collections import deque

def topology_sort():
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

        for i in prerequisite[now]:
            dp[now] = max(dp[now],dp[i])
        dp[now] += cost[now]


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n, k = map(int,sys.stdin.readline().rstrip().split())
    cost = list(map(int,sys.stdin.readline().rstrip().split()))
    graph = [[] for _ in range(n)]
    prerequisite = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]
    dp = [0 for _ in range(n)]
    for i in range(k):
        a, b = map(int,sys.stdin.readline().rstrip().split())
        graph[a-1].append(b-1)
        prerequisite[b-1].append(a-1)
        indegree[b-1] += 1
    target = int(sys.stdin.readline())-1
    topology_sort()
    print(dp[target])

