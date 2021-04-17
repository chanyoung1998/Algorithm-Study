'''
내용:백준 알고리즘 단계별 풀기 투 포인터 1644 소수의 연속합
날짜:21년4월 17일
사용 언어:파이썬
'''
#소수의 집합 생성할 때 에라토스테네스의 체 사용
import sys
import math

def make_prime_numbers(n):
    prime_numbers = [i for i in range(n + 1)]
    primenumbers = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_numbers[i] == 0:
            continue
        j = 2
        while i * j <= n:
            prime_numbers[i * j] = 0
            j += 1

    for i in prime_numbers[2:]:
        if i != 0:
            primenumbers.append(i)
    return primenumbers


n = int(sys.stdin.readline())
if n == 1:
    print(0)
else:
    primenumbers = make_prime_numbers(n)
    end = 0
    sumofprime = primenumbers[0]
    count = 0
    for i in range(len(primenumbers)):

        while sumofprime < n and end < len(primenumbers)-1:
            end += 1
            sumofprime += primenumbers[end]

        if sumofprime == n:
            count += 1

        sumofprime -= primenumbers[i]

    print(count)