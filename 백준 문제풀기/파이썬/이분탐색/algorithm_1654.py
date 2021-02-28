'''
내용:백준 알고리즘 단계별 풀기 이분탐색 1654 랜선 자르기
날짜:21년2월28일
사용 언어:파이썬
'''
#N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
import sys

k, n = map(int,sys.stdin.readline().split())
lengths = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
lengths.sort()


start = 1
end = 2**31 - 1
max_length = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for length in lengths:
        count += length // mid

    if count < n:
        end = mid - 1
    else:
        if max_length < mid:
            max_length = mid
        start = mid + 1

print(max_length)