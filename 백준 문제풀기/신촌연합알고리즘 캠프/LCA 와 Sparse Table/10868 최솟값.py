import sys
import math

n,m = map(int,sys.stdin.readline().rstrip().split())
array = [int(sys.stdin.readline()) for _ in range(n)]
x = math.ceil(math.log2(n))
dp = [[0 for _ in range(n)] for _ in range(x+1)]

def build():
    for j in range(n):
        dp[0][j] = array[j]

    for i in range(1,x+1):
        for j in range(n):
            if j + 2**(i-1) < n:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+2**(i-1)])
            else:
                break
build()
#print(dp)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    a,b = a-1,b-1
    length = b-a+1
    x = math.floor(math.log2(length))
    print(min(dp[x][a],dp[x][b-2**x + 1]))

