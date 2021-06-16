import sys
n = int(sys.stdin.readline())
dp = [[0] * (1 << n) for _ in range(n)]

weight = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(1,n):
    if dp[i][0]:
        dp[i][0] = weight[i][0]
    else:
        dp[i][0] = float('inf')

# dp[curren][route] : current에서 출발하여 route에 있는 도시들을 거쳐 0번 노드로 돌아오는 최단거리
def solution(current,route):

    if dp[current][route] != 0:
        return dp[current][route]

    if route == (1 <<(n-1)) - 1:
        if weight[current][0]:
            return weight[current][0]
        else:
            return float('inf')

    min_dist = float('inf')
    for j in range(1,n):
        if not weight[current][j]:
            continue
        if route & (1 << j - 1):  # route에 j번 째 도시가 포함 되냐? 각 도시는 한 번씩만 포함되어야 하기 때문에 포함되면 안된다.
            continue
        dist = weight[current][j] + solution(j,route | (1 << (j-1)))
        if min_dist > dist:
            min_dist = dist
        dp[current][route] = min_dist

    return min_dist

print(solution(0,0))