'''
내용:백준 알고리즘 단계별 풀기 이분탐색 1654 랜선 자르기
날짜:21년2월28일
사용 언어:파이썬
'''
import sys
n, m = map(int,sys.stdin.readline().split())
lengths = list(map(int,sys.stdin.readline().rstrip().split()))
lengths.sort()

start = 0
end = 2000000000
max_height = -sys.maxsize
while start <= end:
    mid = (start+end)//2
    count = 0
    for length in lengths:
        if length - mid >= 0:
            count += length - mid

    if count < m:
        end = mid - 1
    else:
        if max_height < mid:
            max_height = mid
        start = mid + 1

print(max_height)
