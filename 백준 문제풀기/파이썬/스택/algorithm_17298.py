'''
내용:백준 알고리즘 단계별 풀기 스택 17298 오큰수
날짜:21년1월20일
사용 언어:파이썬
'''
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split(' ')))
stack = []
ret = [-1] * n
for i in range(n):

    while len(stack) != 0 and a[stack[-1]] < a[i]:
        ret[stack.pop()] = a[i]

    stack.append(i)
for i in ret:
    print(i, end= ' ')