'''
24 02 28
괄호 추가하기3
16639
동적계획법
'''
import sys

n = int(sys.stdin.readline())
operations = list(sys.stdin.readline().strip())
dp = [[[0, 0, False] for _ in range(n)] for _ in range(n)]


def getMaxAndMin(i, j):
    if i == j:
        dp[i][j][0] = operations[i]
        dp[i][j][1] = operations[i]
        dp[i][j][2] = True
        return

    if dp[i][j][2]:
        return

    tmpMax = -sys.maxsize
    tmpMin = sys.maxsize
    for x in range(i, j, 2):
        getMaxAndMin(i, x)
        getMaxAndMin(x + 2, j)
        op = operations[x + 1]

        a = eval(dp[i][x][0] + op + dp[x + 2][j][0])
        b = eval(dp[i][x][0] + op + dp[x + 2][j][1])
        c = eval(dp[i][x][1] + op + dp[x + 2][j][0])
        d = eval(dp[i][x][1] + op + dp[x + 2][j][1])

        tmpMax = max(tmpMax,a,b,c,d)
        tmpMin = min(tmpMin,a,b,c,d)

    dp[i][j][0] = str(tmpMax)
    dp[i][j][1] = str(tmpMin)
    dp[i][j][2] = True

getMaxAndMin(0,n-1)
print(dp[0][n-1][0])
#
# for i in range(2, n, 2):
#
#     dp[i][0] = eval(''.join(operations[:i + 1]))
#     dp[i][1] = eval(''.join(operations[:i + 1]))
#     for j in range(0, i, 2):
#
#         operation = ""
#
#         for k in range(j + 1, i + 1):
#             operation += operations[k]
#             if k == j + 1:
#                 operation += '('
#         operation += ')'
#
#         a = str(dp[j][0]) + operation
#         b = str(dp[j][1]) + operation
#
#         dp[i][0] = max(dp[i][0], eval(operation))
#
# print(dp[n - 1])

