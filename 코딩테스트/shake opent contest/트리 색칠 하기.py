import sys
from collections import deque
sys.setrecursionlimit(200001)
def find_parent(root):
    if root:
        for next in adjlist[root]:
            if parent[next] == -1:
                parent[next] = root
                find_parent(next)



def sol():
    ret = 0
    visit = [False for _ in range(n + 1)]
    cur_color = [0 for _ in range(n + 1)]
    q = deque()
    q.append(1)
    visit[1] = True
    while q:
        now = q.popleft()
        if cur_color[now] != color[now]:
            cur_color[now] = color[now]
            ret += 1
            for next in adjlist[now]:
                if next != parent[now]:
                    cur_color[next] = color[now]
                    q.append(next)
        else:
            for next in adjlist[now]:
                if next != parent[now]:
                    cur_color[next] = cur_color[now]
                    q.append(next)



    return ret



n = int(sys.stdin.readline().rstrip())
color = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
adjlist = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]


for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    adjlist[u].append(v)
    adjlist[v].append(u)

parent[1] = 0
find_parent(1)
#print(parent)
print(sol())