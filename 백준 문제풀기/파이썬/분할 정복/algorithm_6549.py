import sys

sys.setrecursionlimit(10 ** 6)


def sol(array, start, end):
    if start >= end:
        return array[start]
    mid_index = 0
    min_value = min(array[start:end+1])
    for i in range(start, end + 1):
        if array[i] == min_value:
            mid_index = i
            break

    right_maxsize = sol(array, start, mid_index - 1)
    if mid_index == end:
        left_maxsize = sol(array, mid_index, end)
    else:
        left_maxsize = sol(array, mid_index + 1, end)
    mid_maxsize = min_value * (end - start + 1)

    return max(right_maxsize, left_maxsize, mid_maxsize)


while True:
    inputs = list(map(int, sys.stdin.readline().rstrip().split()))

    if inputs == [0]:
        break
    n = inputs[0]
    array = inputs[1:]
    print(sol(array, 0, n-1))


