import sys
sys.setrecursionlimit(10000)
def sol(a, b):

    if a == m or b == m:
        return 0

    if dp[a][b] != -1:
        return dp[a][b]

    dp[a][b] = 987654321
    next = max(a,b) + 1

    w1 = abs(accidentsA[next][0] - accidentsA[a][0]) + abs(accidentsA[next][1] - accidentsA[a][1])
    w2 = abs(accidentsB[next][0] - accidentsB[b][0]) + abs(accidentsB[next][1] - accidentsB[b][1])

    p = sol(next, b) + w1
    q = sol(a, next) + w2

    dp[a][b] = min(p,q)

    return dp[a][b]

def print_car(a,b):
    if a == m or b == m:
        return

    next = max(a,b) + 1

    w1 = abs(accidentsA[next][0] - accidentsA[a][0]) + abs(accidentsA[next][1] - accidentsA[a][1])
    w2 = abs(accidentsB[next][0] - accidentsB[b][0]) + abs(accidentsB[next][1] - accidentsB[b][1])

    p = sol(next, b) + w1
    q = sol(a, next) + w2

    if p > q:
        print(2)
        print_car(a,next)
    else:
        print(1)
        print_car(next,b)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
accidents = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(m)]
accidentsA = [(1,1)] + accidents
accidentsB = [(n,n)] + accidents
dp = [[-1 for _ in range(m+2)] for _ in range(m+2)]
sol(0,0)

print(dp[0][0])
print_car(0,0)