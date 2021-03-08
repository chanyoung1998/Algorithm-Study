'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 1520 내리막 길
날짜:21년3월 8일
사용 언어:파이썬
'''
import sys


def dfs(row,column):

        if row == m - 1 and column == n - 1:
            return 1

        if dp[row][column] == -1:
            dp[row][column] = 0

            for i in range(4):
                nrow = row + dx[i]
                ncol = column + dy[i]

                if 0 <= nrow and nrow < m and 0 <= ncol and ncol < n:
                    if heights[row][column] > heights[nrow][ncol]:
                        dp[row][column] += dfs(nrow,ncol)

        return dp[row][column]

m, n = map(int,sys.stdin.readline().split())
heights = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [ -1, 0 ,1 ,0]
dy = [0 , -1, 0 ,1]
print(dfs(0,0))
print(dp)