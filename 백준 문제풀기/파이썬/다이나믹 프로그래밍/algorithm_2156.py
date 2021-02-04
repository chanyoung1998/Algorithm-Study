'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  2156 포도주 시식
날짜:21년2월4일
사용 언어:파이썬
'''
def sol(n):
    if n == 1 or n ==2:
        temp = 0
        for i in range(n):
            temp += arr[i]
        print(temp)
        return

    #임의의로 0번 째 잔을 설정해서 계산
    #dp[n]이랑 arr[n]이랑 인덱싱이 다르다
    #dp(n) = max( dp(n-2) + arr[n-1], dp(n-3)+arr[n-2]+arr[n-1],dp(n-1))
    dp[0] = 0
    dp[1] =arr[0]
    dp[2] =arr[0]+arr[1]
    for i in range(3,n+1):
        dp[i] = max(dp[i-2]+arr[i-1],dp[i-3]+arr[i-2]+arr[i-1],dp[i-1])

    print(dp[n])
    return



dp = [0 for _ in range(10001)]
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sol(n)


