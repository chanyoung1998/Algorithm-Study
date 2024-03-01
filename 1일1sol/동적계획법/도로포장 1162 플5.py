'''
24 02 29
도로포장
1162
플5
다익스트라, dp



'''

import sys
from heapq import heappush,heappop


n, p, k = map(int, sys.stdin.readline().strip().split(' '))
adjlist = [[] for _ in range(n + 1)]

for _ in range(p):
    a, b, c = map(int, sys.stdin.readline().strip().split(' '))
    adjlist[a].append((b, c))
    adjlist[b].append((a, c))

dp = [[sys.maxsize for _ in range(k+1)] for _ in range(n+1)]
pq = []
dp[1][0] = 0
heappush(pq,(dp[1][0],0,1))

while pq:

    curCost, curK, curNode = heappop(pq)

    if dp[curNode][curK] < curCost:
        continue

    for nextNode, nextCost in adjlist[curNode]:

        if dp[nextNode][curK] > curCost + nextCost:
            dp[nextNode][curK] = curCost + nextCost
            heappush(pq,(dp[nextNode][curK], curK, nextNode))

        if curK + 1 <= k and dp[nextNode][curK+1] > curCost:
            dp[nextNode][curK+1] = curCost
            heappush(pq,(dp[nextNode][curK+1], curK+1,nextNode))


print(min(dp[n]))