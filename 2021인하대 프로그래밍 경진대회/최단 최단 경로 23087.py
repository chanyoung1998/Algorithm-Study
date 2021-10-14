import sys

n, m, x, y = map(int, sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append((v,w))

#다익스트라 + alpha