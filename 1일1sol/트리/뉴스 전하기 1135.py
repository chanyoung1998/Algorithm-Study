'''
24 03 22
뉴스 전하기
1135
골2
트리, dp, 그리디
'''
import sys
from heapq import heappush,heappop

n = int(sys.stdin.readline())
parents = list(map(int,sys.stdin.readline().strip().split(' ')))
adjlist = [[] for _ in range(n)]
visit = [0 for _ in range(n)]

for i in range(1,n):
    adjlist[parents[i]].append(i)

def foo(curNode):

    if len(adjlist[curNode]) == 0:
        return 0

    pq = []
    for nextNode in adjlist[curNode]:
        heappush(pq,-foo(nextNode))

    i = 1
    while pq:
        time = -1 * heappop(pq)
        visit[curNode] = max(visit[curNode], time + i)
        i += 1

    return visit[curNode]

foo(0)
print(visit[0])

