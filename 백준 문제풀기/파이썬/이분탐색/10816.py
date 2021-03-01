import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

array.sort()

for t in target:
    s = 0
    e = len(array) - 1
    while s < e:
        m = (s + e) // 2
        if array[m] > t:
            e = m
        else:
            s = m + 1
    # t를 초과한 값이 처음 나오는 위치
    upper_bound = e

    s = 0
    e = len(array) - 1
    while s < e:
        m = (s + e) // 2
        if array[m] >= t:
            e = m
        else:
            s = m + 1
    # t이상인 값이 처음 나오는 위치
    lower_bound = e



    if upper_bound == n-1 and array[upper_bound] == t:
        print(upper_bound - lower_bound + 1, end=' ')
    elif upper_bound != lower_bound:
        print(upper_bound - lower_bound, end=' ')
    elif upper_bound == lower_bound:
        print(0, end=' ')



