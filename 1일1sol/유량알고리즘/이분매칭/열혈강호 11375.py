import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
adjlist = []
jobs = [-1 for _ in range(m)]
visit = [False for _ in range(m)]
for _ in range(n):
    inputs = list(map(lambda x:int(x)-1,sys.stdin.readline().rstrip().split()))
    adjlist.append(inputs[1:])



def dfs(x):
    for next in adjlist[x]:
        if visit[next]:
            continue

        visit[next] = True
        if jobs[next] == -1 or dfs(jobs[next]):
            jobs[next] = x
            return True

    return False

cnt = 0
for i in range(n):
    visit = [False for _ in range(m)]
    if dfs(i):
        cnt += 1
print(cnt)