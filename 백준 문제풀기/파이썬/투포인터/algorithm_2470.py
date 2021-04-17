'''
내용:백준 알고리즘 단계별 풀기 투 포인터 2470번 두 용액
날짜:21년4월 14일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline())
liquids = list(map(int,sys.stdin.readline().rstrip().split()))
liquids.sort()
end = n - 1
ret_min = sys.maxsize
ret1 = 0
ret2 = 0
for start in range(n):
    if start >= end:
        break
    if liquids[start] + liquids[end] < 0 :
        if ret_min > abs(liquids[start] + liquids[end]):
            ret_min = abs(liquids[start] + liquids[end])
            ret1 = start
            ret2 = end
        continue

    while liquids[start] + liquids[end] > 0 and start < end:
        end -= 1
    if ret_min > abs(liquids[start] + liquids[end]) and start != end:
        ret_min = abs(liquids[start] + liquids[end])
        ret1 = start
        ret2 = end
    if ret_min > abs(liquids[start] + liquids[end+1]) and start != end+1:
        ret_min = abs(liquids[start] + liquids[end+1])
        ret1 = start
        ret2 = end+1

print(liquids[ret1],liquids[ret2],sep=' ')