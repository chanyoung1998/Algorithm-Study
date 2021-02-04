'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  2579 계단 오르기
날짜:21년2월4일
사용 언어:파이썬
'''

def sol(n):
    if n == 1:
        print(arr[0])
        return
    if n == 2:
        print(arr[0]+arr[1])
        return

    dp[0] = 0
    dp[1] = arr[0]
    dp[2] = arr[1]+arr[0]
    for i in range(3,n+1):
        dp[i] = max(dp[i-3]+arr[i-2]+arr[i-1],dp[i-2]+arr[i-1])

    print(dp[n])
    return


dp = [0 for _ in range(301)]
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sol(n)