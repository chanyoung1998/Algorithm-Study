''' 
내용:백준 알고리즘 재귀단계 10870 피보나치수 5
날짜:21년1월16일 
사용 언어:파이썬
'''
def Fibonacci(n:int):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
       return Fibonacci(n-1)+Fibonacci(n-2)

n = int(input())
print(Fibonacci(n))