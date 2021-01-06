''' 
내용:백준 알고리즘 단계별 풀기 입출력과 사칙연산 10430번
날짜:21년1월5일 
사용 언어:파이썬
'''

num1,num2,num3 = input().split()

A = int(num1)
B = int(num2)
C = int(num3)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
