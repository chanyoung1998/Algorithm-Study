'''
내용:백준 알고리즘 단계별 풀기 이분탐색  2110 공유기 설치
날짜:21년2월28일
사용 언어:파이썬
'''
#가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다

import sys

n, c = map(int,sys.stdin.readline().split())
locations = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
locations.sort()

max_distance = -sys.maxsize
start = 0
end = 1000000000

while start <= end:
    mid = (start+end)//2
    # 가장 왼쪽 집에 공유기를 이미 하나 설치했다고 가정 (최대한 설치하기 위해서는 첫 번째 집에 설치하면서 시작하는 것이 좋다)
    count = 1
    last = locations[0]
    for location in locations[1:]:
        if location - last >= mid:
            count += 1
            last = location

    if count < c:
        end = mid - 1
    else:
        if mid > max_distance:
            max_distance = mid
        start = mid + 1

print(max_distance)
