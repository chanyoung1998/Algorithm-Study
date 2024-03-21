import sys


N,K = map(int,sys.stdin.readline().strip().split(' '))
checKPoints = [tuple(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]

distances = [[0 for _ in range(N)] for _ in range(N)]
dp = [[-1 for _ in range(K+1)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        distances[i][j] = abs(checKPoints[i][0] - checKPoints[j][0]) + abs(checKPoints[i][1] - checKPoints[j][1])


# dp[n][k] : n 번 checkpoint에서 지금까지 k개의 checkpoint를 건너 왔을 때 끝까지 같을 때 거리의 최솟값
def dfs(curCp, cnt):
    if curCp == N-1:
        return 0

    if dp[curCp][cnt] != -1:
        return dp[curCp][cnt]

    orginal = cnt
    dp[curCp][orginal] = sys.maxsize

    for nextCp in range(curCp+1, N):
        if cnt < K:
            dp[curCp][orginal] = min(dp[curCp][orginal],distances[curCp][nextCp] + dfs(nextCp,cnt))
            cnt += 1

        else:
            dp[curCp][orginal] = min(dp[curCp][orginal],distances[curCp][nextCp] + dfs(nextCp,cnt))
            break

    return dp[curCp][orginal]





print(dfs(0,0))

