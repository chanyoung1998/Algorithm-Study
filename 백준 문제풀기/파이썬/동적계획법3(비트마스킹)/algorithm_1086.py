import sys
import math


n = int(sys.stdin.readline())
sets = [int(sys.stdin.readline()) for _ in range(n)]
k = int(sys.stdin.readline())
dp = [[-1 for _ in range(k)] for _ in range(1<<n)]
length = []

for i in range(n):
    length.append(len(str(sets[i])))
# rm을 미리 계산 해놔야 시간 초과를 피할 수 있다.
# 수가 너무 커서 시간을 너무 많이 잡아먹는다
rm = [[-1 for _ in range(sum(length))] for _ in range(n)]
for i in range(n):
    for j in range((sum(length))):
        rm[i][j] = (sets[i] * 10 ** j) % k


# dp[bitfield][mod]
def sol(l,bit,mod):

    if bit == (1 << n) - 1:
        if mod == 0:
            return 1
        else:
            return 0

    if dp[bit][mod] != -1:
        return dp[bit][mod]


    dp[bit][mod] = 0
    for i in range(n):
        if bit & 1 << i == 0:
            dp[bit][mod] += sol(l + length[i], bit | 1 << i, (mod + rm[i][l]) % k)
        # rm배열 없을 때 코드
        # dp[bit][mod] += sol(length + length[i],bit | 1 << i, (mod+(sets[i]%k)*(10**length)) % k)

    return dp[bit][mod]

temp = sol(0,0,0)
F = math.factorial(n)
if temp==0:
    print('0/1')
else:
    if temp == F:
        print('1/1')
    else:
        v=math.gcd(F,dp[0][0])
        print('{}/{}'.format(temp//v,F//v))