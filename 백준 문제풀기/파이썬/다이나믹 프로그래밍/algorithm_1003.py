'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍 1003 피보나치
날짜:21년2월2일
사용 언어:파이썬
'''

'''
def fibonacci(n):
    if n == 1 or n ==0:
        print('fibonacci('+str(n)+')')
        count[n] += 1
        return n
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]'''

dp = [0 for _ in range(41)]
dp[0] = [1,0]
dp[1] =[0,1]
def fibonacci(n):

    if n == 0:
        return dp[0]
    if n == 1:
        return dp[1]

    for i in range(2,n+1):
        if dp[i] != 0:
            continue
        count_0 = dp[i-1][0] + dp[i-2][0]
        count_1 = dp[i-1][1] + dp[i-2][1]
        dp[i] = [count_0,count_1]
    return dp[n]

T = int(input())
test_case = []
for i in range(T):
    test_case.append(int(input()))
for tc in test_case:
    print(*fibonacci(tc))

