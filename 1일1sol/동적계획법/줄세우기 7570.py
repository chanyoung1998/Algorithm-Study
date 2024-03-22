import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().strip().split(' ')))
index = [0 for _ in range(n+1)]
for i in range(n):
    index[numbers[i]] = i


dp = [1 for _ in range(n+1)]
for i in range(2,n+1):

    if index[i-1] < index[i]:
        dp[i] = dp[i-1] + 1

print(n-max(dp))
