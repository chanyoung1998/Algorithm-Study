'''
내용:백준 알고리즘 단계별 풀기 동적계획과 최단거리의 역추적 14002 가장 긴 증가하는 부분 수열4
날짜:21년4월 17일
사용 언어:파이썬
'''

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().rstrip().split()))
temp = [[array[0]]]

for i in array[1:]:
    check = False
    for temp_lcs in temp:
        if temp_lcs[-1] < i:
            temp_lcs.append(i)
        else:
            check = True

    for temp_lcs in temp:
        pass

    if check:
        temp.append([i])


