import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
adjlist = []
jobs = [0 for _ in range(n+1)]
visit = [False for _ in range(n+1)]
for _ in range(n):
    inputs = list(map(int,sys.stdin.readline().rstrip().split()))
    adjlist.append(inputs[1:])



def dfs(x):
    for next in adjlist[x]:
        if visit[next]:
            continue

        visit[next] = True
        if jobs[next] == 0 or dfs(jobs[next]):
            jobs[next] = x
            return True

    return False


 