# 이 방법은 약 60%에서 시간초과가 발생한다.

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

array.sort()
ret = []
for t in target:
    s = 0
    e = len(array) - 1
    flag = False
    while s <= e:
        m = (s + e) // 2
        if array[m] == t:
            flag = True
            break
        elif array[m] > t:
            e = m - 1
        elif array[m] < t:
            s = m + 1

    if not flag:
        ret.append(0)
    else:
        count = 0
        nl = m
        nr = m + 1
        while True:
            if (nl < 0 or array[nl] != t) and (nr > n - 1 or array[nr] != t):
                break
            elif nl < 0 or array[nl] != t:
                if array[nr] == t:
                    count += 1
                nr += 1
            elif nr > n - 1 or array[nr] != t:
                if array[nl] == t:
                    count += 1
                nl -= 1
            else:
                if array[nr] == t:
                    count += 1
                if array[nl] == t:
                    count += 1
                nr += 1
                nl -= 1

        ret.append(count)

print(*ret)


