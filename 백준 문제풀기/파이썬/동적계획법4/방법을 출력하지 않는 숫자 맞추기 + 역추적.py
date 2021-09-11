import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())

cur_state = list(map(int,list(sys.stdin.readline().rstrip())))
tar_state = list(map(int,list(sys.stdin.readline().rstrip())))

dp = [[-1 for _ in range(11)] for _ in range(n)]
path = [[0 for _ in range(11)] for _ in range(n)]
# dp[i][j]를 i번째 숫자나사가 왼쪽으로 j번 돌아간 상황에서 회전칸수의 최소라고 하자.
def sol(i,j):
    if i == n:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize

    lcnt = (tar_state[i]-cur_state[i] - j + 20) % 10
    rcnt = (10 - lcnt)
    # dp[i][j] = min(sol(i+1,(j+lcnt) % 10) + lcnt, sol(i+1,j) + rcnt)

    lc = sol(i+1,(j+lcnt) % 10) + lcnt
    rc = sol(i+1,j) + rcnt
    if lc < rc:
        dp[i][j] = lc
        path[i][j] = lcnt
    else:
        dp[i][j] = rc
        path[i][j] = -rcnt
    return dp[i][j]

print(sol(0,0))
#print(path)
lcnt = 0
for i in range(n):
    print(i + 1, path[i][lcnt])
    if path[i][lcnt] > 0:
        lcnt =(lcnt+path[i][lcnt]) % 10


