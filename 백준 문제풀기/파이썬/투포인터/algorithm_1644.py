'''
내용:백준 알고리즘 단계별 풀기 투 포인터 1644 소수의 연속합
날짜:21년4월 14일
사용 언어:파이썬
'''
#소수의 집합 생성할 때 에라토스테네스의 체 사용
import sys

n = int(sys.stdin.readline())
prime_numbers = [i for i in range(1,n+1)]

for i in range(2,n+1):
    if prime_numbers[i] == 0:
        continue
    for j in range(i+1,n+1,i):
        prime_numbers[j] = 0