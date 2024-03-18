'''
24 03 18
함께 블록 쌓기
18427
골4
동적계획법, 냅색
'''

import sys

N,M,H  = map(int,sys.stdin.readline().strip().split(' '))
blocks = [list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
dp = [[-1 for _ in range(H+1)] for _ in range(N)]


ret = 0

def func(x,curHeight):
    global ret

    if curHeight == H:
        return 1

    if x == N:
        return 0

    if dp[x][curHeight] != -1:
        return dp[x][curHeight]



    dp[x][curHeight] = 0

    for h in blocks[x]:
        if curHeight + h <= H:
            dp[x][curHeight] += func(x+1,curHeight+h)

    dp[x][curHeight] += func(x+1,curHeight)
    dp[x][curHeight] = dp[x][curHeight] % 10007


    return dp[x][curHeight]


func(0,0)

print(dp[0][0])