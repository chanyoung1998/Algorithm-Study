import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
cows = []
visit = [False for _ in range(m)]
d =[-1 for _ in range(m)]
for _ in range(n):
    cows.append(list(map(lambda x:int(x) - 1,sys.stdin.readline().rstrip().split()))[1:])


def dfs(cur):

    for next in cows[cur]:
        if visit[next]:
            continue

        visit[next] = True
        if d[next] == -1 or dfs(d[next]):
            d[next] = cur
            return True

    return False

cnt = 0
for i in range(n):
    # i가 _번째 축사 방문했는 지 안 했는지 검사하는 것
    visit = [False for _ in range(m)]
    if dfs(i):
        cnt += 1

print(cnt)