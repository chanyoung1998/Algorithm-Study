'''
24 7 30
사칙연산
프로그래머스
동적계획법
'''
import sys


def solution(arr):
    answer = -1
    dp = [[[] for _ in range(len(arr))] for _ in range(len(arr))]
    for rang in range(0, len(arr), 2):
        for start in range(0, len(arr) - rang, 2):
            dp[start][start + rang] = [getMin(dp, arr, start, start + rang), getMax(dp, arr, start, start + rang)]

    return dp[0][len(arr)-1][1]


def getMin(dp, arr, a, b):
    if a == b:
        return int(arr[a])
    minValue = sys.maxsize
    for i in range(a, b, 2):
        op = arr[i + 1]
        for x in dp[a][i]:
            for y in dp[i + 2][b]:
                minValue = min(minValue, eval(x, y, op))

    return minValue


def getMax(dp, arr, a, b):
    if a == b:
        return int(arr[a])
    maxValue = -sys.maxsize
    for i in range(a, b, 2):
        op = arr[i + 1]
        for x in dp[a][i]:
            for y in dp[i + 2][b]:
                maxValue = max(maxValue, eval(x, y, op))

    return maxValue


def eval(a, b, op):
    if op == "-":
        return int(a) - int(b)
    elif op == "+":
        return int(a) + int(b)


# (a,b) 구간 최솟값 dp[a][b][0] = dp[a][b-1],dp[b][b]
# (a,b) 구간 최댓값 dp[a][b][1] =
# 0 1 2 3 4 5 6
# [0,6] -> [0,0] [2,6] , [0,2] [4,6],  [0,4] [6,6]
assert solution(["1", "-", "3", "+", "5", "-", "8"]) == 1
assert solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]) == 3
