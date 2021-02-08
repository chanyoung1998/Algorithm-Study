'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍 9251 LCS
날짜:21년2월8일
사용 언어:파이썬
'''

str1 = input()
str2 = input()
dp =[[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for s1,i in zip(str1,range(1,len(str1)+1)):
    for s2,j in zip(str2,range(1,len(str2)+1)):
        if s1 == s2:
            dp[i][j] = dp[i-1][j-1]+1
        elif s1 != s2:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[len(str1)][len(str2)])
