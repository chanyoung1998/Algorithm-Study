'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  1912 연속합
날짜:21년2월8일
사용 언어:파이썬

'''
import sys


n = int(input())
arr = list(map(int,input().split(' ')))

#시간 초과
'''temp = -sys.maxsize
for i in range(n):
    dp = []
    dp.append(arr[i])
    for j in range(1,n-i):
        dp.append(dp[len(dp)-1]+arr[i+j])
    temp = max(temp,max(dp))
print(temp)'''


#메모리초과
'''dp = []

for i in range(n):
    dp.append([0] * (n-i))

for i in range(n):
    dp[i][0] = arr[i]
    for j in range(1,n-i):
        dp[i][j] = dp[i][j-1]+arr[i+j]

t = -sys.maxsize
for x in dp:
    t = max(max(x),t)
print(t)'''


'''
Dynamic Programming으로 접근한다.

첫 번째 정수까지의 최대 연속 부분 합을 구한다. 당연히 그 값 그대로.

두 번째 정수까지의 최대  연속 부분 합을 구한다.

n 번째 정수까지의 최대 연속 부분 합을 구한다.

n 번째 정수까지의 최대 연속 부분 합을 D(n)이라고 하자.
쉽게 생각했을 때, D(n)은 D(n-1) + n 번째 정수이다.
그러나, D(n-1) + n이 n보다 작다면 n을 더해나가는 게 의미가 없다.
이 경우에는 D(n)은 n이 된다.
'''

sum = [arr[0]]
for i in range(len(arr) - 1):
    sum.append(max(sum[i] + arr[i + 1], arr[i + 1]))
print(max(sum))
