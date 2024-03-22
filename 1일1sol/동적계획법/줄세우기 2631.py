import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))