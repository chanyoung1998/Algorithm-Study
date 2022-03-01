import sys

def dfs(cur):

    if visit[cur]:
        return False

    visit[cur] = True


    for nxt in adj[cur]:

        if d[nxt] == -1:
            if visit[nxt]:
                continue
            d[cur] = nxt
            d[nxt] = cur
            return True

        elif dfs(d[nxt]):
            d[nxt] = cur
            d[cur] = nxt
            return True


    return False


testcase = int(sys.stdin.readline())

for _ in range(testcase):
    n,w = map(int,sys.stdin.readline().rstrip().split())
    enemy = []
    enemy += list(map(int,sys.stdin.readline().rstrip().split()))
    enemy += list(map(int, sys.stdin.readline().rstrip().split()))
    adj = [[] for _ in range(2 * n)]
    visit = [False for _ in range(2*n)]
    d = [-1 for _ in range(2*n)]
    cnt = 2 * n

    if n == 1:
        if sum(enemy) <= w:
            print(1)
        else:
            print(0)
        continue

    for i in range(2*n):
        if 0 <= i < n:
            if enemy[i] + enemy[(i-1) % n] <= w:
                adj[i].append((i-1) % n)

            if enemy[i] + enemy[(i+1) % n] <= w:
                adj[i].append((i+1) % n)

            if enemy[i] + enemy[(i+n)] <= w:
                adj[i].append((i+n))

        elif n < i < 2*n-1:
            if enemy[i] + enemy[(i - 1)] <= w:
                adj[i].append((i - 1))

            if enemy[i] + enemy[(i + 1) ] <= w:
                adj[i].append((i + 1))

            if enemy[i] + enemy[(i -n)] <= w:
                adj[i].append((i - n))
        elif i == n:
            if enemy[i] + enemy[2*n - 1] <= w:
                adj[i].append(2*n - 1)

            if enemy[i] + enemy[i+1] <= w:
                adj[i].append(i+1)

            if enemy[i] + enemy[(i-n)] <= w:
                adj[i].append(i-n)
        elif i == 2 * n - 1:
            if enemy[i] + enemy[i-1] <= w:
                adj[i].append((i-1))

            if enemy[i] + enemy[n] <= w:
                adj[i].append(n)

            if enemy[i] + enemy[i-n] <= w:
                adj[i].append(i-n)




    for i in range(2 * n):
        visit = [False for _ in range(2*n)]
        if d[i] == -1:
            if dfs(i):
                # print(i)
                cnt -= 1

    # print(d)

    print(cnt)



