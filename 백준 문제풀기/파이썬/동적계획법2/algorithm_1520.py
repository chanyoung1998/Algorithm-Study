'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 1520 내리막 길
날짜:21년3월 8일
사용 언어:파이썬
'''
import sys

#시간 초과 발생
def dfs(row,column):
    global count
    if row == m - 1 and column == n - 1:
        count += 1
        return
    else:
        height = heights[row][column]
        if row > 0 and heights[row-1][column] < height:
            dfs(row-1,column)
        if row < m - 1 and heights[row+1][column] < height:
            dfs(row+1,column)
        if column > 0 and heights[row][column-1] < height:
            dfs(row,column-1)
        if column < n - 1 and  heights[row][column+1] < height:
            dfs(row,column+1)
        return


m, n = map(int,sys.stdin.readline().split())
heights = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
count = 0
dfs(0,0)
print(count)