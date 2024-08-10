'''
24 8 01
도둑질
프로그래머스
동적계획법
'''
import sys


# len(money) <= 1000000

def solution(money):

    dp = [0 for _ in range(len(money))]

    for i in range(len(money)-1):
        dp[i] = max(money[i]+dp[i-2],dp[i-1])

    dp2 = [0 for _ in range(len(money))]

    for i in range(1,len(money)):
        dp2[i] = max(money[i]+dp2[i-2],dp2[i-1])


    return max(max(dp),max(dp2))











assert solution([1, 2, 3, 1]) == 4
