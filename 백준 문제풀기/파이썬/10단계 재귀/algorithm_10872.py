''' 
내용:백준 알고리즘 재귀단계 10872 팩토리얼
날짜:21년1월16일 
사용 언어:파이썬
'''
def factorial(n : int):
    if n ==0 or  n == 1:
        return 1
    else:
        return n*factorial(n-1)


n = int(input())
result = factorial(n)
print(result)
