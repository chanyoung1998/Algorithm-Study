'''
내용:백준 알고리즘 단계별 풀기 투 포인터 3273번 두수의 합
날짜:21년4월 14일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().rstrip().split()))
array.sort()
x = int(sys.stdin.readline())

start = 0
end = n-1
count = 0
while start < end :
    if array[start] + array[end] < x:
        start += 1
    elif array[start] + array[end] > x:
        end -= 1
    else:
        start += 1
        end -= 1
        count += 1
print(count)