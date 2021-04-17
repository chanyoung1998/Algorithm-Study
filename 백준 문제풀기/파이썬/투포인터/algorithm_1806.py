'''
내용:백준 알고리즘 단계별 풀기 투 포인터 1806번 부분합
날짜:21년4월 14일
사용 언어:파이썬
'''

import sys

n, s = map(int,sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))
start = 0
end = 0
min_length = n+1
sum = array[start]
for start in range(n):
    while sum < s and end < n-1:
        end += 1
        sum += array[end]

    if sum >= s:
        min_length = min(min_length,end-start + 1)

    sum -= array[start]


print(min_length if min_length != n+1 else 0)