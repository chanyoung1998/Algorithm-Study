import sys,math

m = int(sys.stdin.readline())
array = list(map(lambda x:x-1,map(int,sys.stdin.readline().rstrip().split())))
q = int(sys.stdin.readline())
# x = 18
x = math.floor(math.log2(500000))
dp = [[0 for _ in range(x+1)] for _ in range(m)]


def build(dp):
    for i in range(m):
        dp[i][0] = array[i]

    for k in range(1,x+1):
        for i in range(m):
            dp[i][k] = dp[dp[i][k-1]][k-1]


build(dp)
for _ in range(q):
    n,a = map(int,sys.stdin.readline().rstrip().split())
    a = a-1
    x = math.ceil(math.log2(n))
    ret = []
    #방법1
    '''while x >= 0:
        if 2**x > n:
            x -= 1
        else:
            ret.append(x)
            n -= 2**x
            x -= 1
    temp = dp[a][ret[-1]]
    if len(ret) > 1:
        for i in ret[-2::-1]:
            temp = dp[temp][i]
    print(temp+1)'''
    #방법2
    '''for j in range(18, -1, -1):
        if n >= (1 << j):
            n -= (1 << j)
            a = dp[a][j]
    print(a+1)'''

    while x >= 0:
        if 2 ** x > n:
            x -= 1
        else:
            a = dp[a][x]
            n -= 2 ** x
            x -= 1

    print(a+1)



