'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍 1904 01타일\
날짜:21년2월2일
사용 언어:파이썬
'''
dp = [0 for _ in range(1000001)]
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1] +dp[i-2]) % 15746 #15746을 안해주면 나중에 숫자가 커지면 메모리초과오류가 날 수도 있음
    print(dp[n] % 15746)