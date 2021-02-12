'''
내용:백준 알고리즘 단계별 풀기 그리디 11399 ATM
날짜:21년2월12일
사용 언어:파이썬
'''

n = int(input())
p = list(map(int,input().split()))
p.sort()
sum = 0
temp = 0
for time in p:
    temp += time
    sum += temp
print(sum)
