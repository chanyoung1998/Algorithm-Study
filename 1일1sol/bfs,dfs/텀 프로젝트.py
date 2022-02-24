import sys
sys.setrecursionlimit(100000)
def dfs(x):
    global cnt
    visit[x] = True
    next = student[x]
    if not visit[next]:
        dfs(next)
    else:
        if not finish[next]:
            cnt += 1 # 자기 자신
            tmp = next
            while tmp != x:
                tmp = student[tmp]
                cnt += 1

    finish[x] = True

    return






t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    student = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
    visit = [False for _ in range(n+1)]
    finish = [False for _ in range(n+1)]
    cnt = 0

    for i in range(1,n+1):
        if not visit[i]:
            dfs(i)

    print(n-cnt)