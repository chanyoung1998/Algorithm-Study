'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  9461 파도반 수열
날짜:21년2월2일
사용 언어:파이썬
'''
def Crocus(n):
    if n == 1 or n==2 or n==3:
        return dp[n]
    else:
        if dp[n] != 0:
            return dp[n]
        for i in range(n+1):
            if dp[i] != 0:
                continue
            dp[i] = dp[i-2]+dp[i-3]
        return dp[n]



dp =[0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
n = int(input())
test_case = []
for i in range(n):
    test_case.append(int(input()))
for tc in test_case:
    print(Crocus(tc))

