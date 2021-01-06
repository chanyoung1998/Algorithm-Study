''' 
내용:백준 알고리즘 단계별 풀기 입출력과 사칙연산 2588번
날짜:21년1월5일 
사용 언어:파이썬
'''

num1 = input()
num2 = input()
A = int(num1)
B = int(num2)

B1 = B//100
B2 = (B%100)//10
B3 = (B%10)

print(A*B3)
print(A*B2)
print(A*B1)
print(A*B)
