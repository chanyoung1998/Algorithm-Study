import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n)]
job = [-1 for _ in range(m)]
visit = [False for _ in range(m)]
for i in range(n):
    adjlist[i] = list(map(lambda x :int(x)-1,sys.stdin.readline().rstrip().split()))[1:]

def dfs(cur):

    for next in adjlist[cur]:
        if visit[next]:
            continue

        visit[next] = True

        if job[next] == -1 or dfs(job[next]):
            job[next] = cur
            return True

    return False


cnt = 0
for i in range(n):
    visit = [False for _ in range(m)]
    if dfs(i):
       cnt += 1
    visit = [False for _ in range(m)]
    if dfs(i):
        cnt += 1
print(cnt)
# print(job)