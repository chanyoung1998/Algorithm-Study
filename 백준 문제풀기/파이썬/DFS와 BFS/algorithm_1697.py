'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 1697  숨바꼭질
날짜:21년3월 15일
사용 언어:파이썬
'''
import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
dp = [0 for _ in range(100001)]
dp[n] = 1
queue = deque()
queue.append(n)

operations = [1,-1,2]

# n을 뿌리로 하는 트리를 그려 보아라 자식 노드는 부모 노드에서 나올 수 있는 연산 3가지이다
# 계속 그리다가 k가 처음으로 나오는 단계가 있을 것. 처음으로 이 k가 나오는 단계가 가장 최소한의 방법으로 n에서 k를 찾을 수 있는 방법이다.
# 이제 이것을 바탕으로 너비 우선 탐색을 진행하자. ( 깊이 우선 탐색을 하면 안되는 이유는 이 트리의 깊이는 거의 무한이기 때문에.. 무한루프에 빠진다)

while queue:
    # dp[k]가 0이 아니라는 것은 방문 되었다는 것
    if dp[k] != 0:
        break
    x = queue.popleft()
    for op in operations:
        q = x + op
        if op == 2:
            q = x * op
        # dp[q]가 0이 아니라는 것은 이미 이전 깊이에서 n에서 부터에 최소한의 단계인 dp[q]값을 찾았다는 의미이기 때문에 더이상 찾을 필요 없다.
        if 0 <= q <= 100000 and dp[q] == 0:
            dp[q] = dp[x] + 1
            queue.append(q)


# dp[n]을 1로 맨처음에 설정했기 때문에 1을 빼줘야 한다
print(dp[k]-1)