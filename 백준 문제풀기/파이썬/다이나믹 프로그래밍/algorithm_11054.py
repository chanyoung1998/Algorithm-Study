'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  11054 가장 긴 바이토닉 수열
날짜:21년2월8일
사용 언어:파이썬
'''

n = int(input())
A = list(map(int,input().split()))
A_dsd = A[::-1]
dp_asd = [0 for _ in range(1001)]
dp_dsd = [0 for _ in range(1001)]

for i in range(n):
    temp = [0]
    for j in range(i):
        if A[i] > A[j]:
            temp.append(dp_asd[j])
    dp_asd[i] = max(temp) + 1


for i in range(n):
    temp = [0]
    for j in range(i):
        if A_dsd[i] > A_dsd[j]:
            temp.append(dp_dsd[j])
    dp_dsd[i] = max(temp) + 1

sum = 0
for i in range(n):
    temp = dp_asd[i] + dp_dsd[(n-1)-i]
    if temp > sum:
        sum = temp
print(sum-1)

