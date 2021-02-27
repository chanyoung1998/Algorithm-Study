import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

array.sort()

for t in target:
    s = 0
    e = len(array) - 1
    flag = False
    while s <= e:
        m = (s + e) // 2
        if array[m] == t:
            print(1)
            flag = True
            break
        elif array[m] > t:
            e = m - 1
        elif array[m] < t:
            s = m + 1

    if not flag:
        print(0)
