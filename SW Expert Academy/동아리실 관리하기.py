mod = 1000000007
for t in range(int(input())):
    string = input().rstrip()

    dp = [[0 for _ in range(16)] for _ in range(len(string))]

    for i in range(1,16):
        if i & 1 and i & 1 << ord(string[0])-ord('A'):
            dp[0][i] = 1

    # dp[j][i] = sum(dp[j-1][k]) k랑 i는 겹쳐야 함
    for j in range(1,len(string)):
        for i in range(1,16):

            if i & 1 << ord(string[j])-ord('A'):
                for k in range(1,16):
                    if i & k:
                        dp[j][i] += dp[j-1][k]
                        dp[j][i] %= mod

    print('#',t+1,' ',sum(dp[len(string)-1])%mod,sep='')
