'''
내용:백준 알고리즘 단계별 풀기 분할 정복 1629 곱샘
날짜:21년2월23일
사용 언어:파이썬
'''

def power(a,n,c):
    if n == 0:
        return 1
    elif n == 1:
        return a % c

    x = power(a, n //2,c)

    if n % 2 == 0:
        return x * x % c
    else:
        return x * x * a % c

a,b,c = map(int,input().split())
print(power(a,b,c))