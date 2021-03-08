'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 2629 양팔저울
날짜:21년3월 8일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline())
weights = list(map(int,sys.stdin.readline().split()))
t = int(sys.stdin.readline())
tests = list(map(int,sys.stdin.readline().split()))
s =[0,weights[0]]

for i in range(1,n):
    temp = []
    for k in s:
        temp.append(k)
        temp.append(k+weights[i])
        temp.append(abs(k-weights[i]))
    s = list(set(temp))
for test in tests:
    if test in s:
        print('Y',end=' ')
    else:
        print('N',end=' ')
