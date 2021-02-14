'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 1676 팩토리얼 0의 개수
날짜:21년2월14일
사용 언어:파이썬
'''
n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i

fact = str(fact)[::-1]
count = 0
for i in fact:
    if i == '0':
        count += 1
    else:
        break
print(count)
