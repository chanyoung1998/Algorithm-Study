import sys
from collections import deque
n,r,q = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v =map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append(v)
    adjlist[v].append(u)

def inorder(node):
    if node == None:
        return 0