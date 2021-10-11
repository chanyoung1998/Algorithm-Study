import sys
sys.setrecursionlimit(123460)
n = int(sys.stdin.readline().rstrip())
island = [[] for _ in range(n+1)]
adjlist = [[] for _ in range(n+1)]

visit = [False for _ in range(n+1)]
for i in range(n-1):
    ti, ai, pi = sys.stdin.readline().rstrip().split()
    ai, pi = int(ai), int(pi)
    island[i+2] = [ti,ai,pi]
    adjlist[i+2].append(pi)
    adjlist[pi].append(i+2)
island[1] = [0,0,0]
def dfs(node):

    visit[node] = True

    if node == 1:
        island[node][1] = 0
    elif island[node][0] == 'S':
        island[node][1] = island[node][1]
    elif island[node][0] == 'W':
        island[node][1] = -island[node][1]


    for next in adjlist[node]:
        if not visit[next]:
            dfs(next)
            if island[next][1] > 0:
                island[node][1] += island[next][1]

dfs(1)
print(island[1][1])