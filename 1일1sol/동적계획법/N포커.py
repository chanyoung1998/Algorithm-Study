'''
24 02 22
N포커
골2
DP,조합론,포함배제의 원리
'''

N = int(input())
MOD = 10007
combi = [[0 for _ in range(53)] for _ in range(53)]
dp = [0 for _ in range(53)]
for i in range(53):
    combi[i][0] = 1

for i in range(1,53):
    for j in range(1,i+1):
        combi[i][j] = (combi[i-1][j] + combi[i-1][j-1]) % MOD

for n in range(53):
    ans = 0
    for i in range(1,n):
        if 4*i <= n:
            ans += (-1) ** (i+1) * combi[13][i] * combi[52-4*i][n-4*i]

    dp[n] = ans % MOD

print(dp[N])
