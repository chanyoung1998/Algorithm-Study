'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 11066 파일 합치기
날짜:21년3월4일
사용 언어:파이썬
'''
# 틀린 풀이
# 일단 sort하면 안된다. 인접한 장끼리만 합치는 것이 가능하기 때문
# 그리고 sort해도 된다해도 최솟 값이 될 수 없다.
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    costs = list(map(int,sys.stdin.readline().rstrip().split()))
    costs.sort()

    dp = [0 for _ in range(k)]
    dp[0] = costs[0]
    dp[1] = costs[0] + costs[1]
    for i in range(2,k):
        dp[i] = min(2 * (dp[i-2] + costs[i - 1] + costs[i]), (2 * dp[i-1] + costs[i]))
    print(dp[k-1])

