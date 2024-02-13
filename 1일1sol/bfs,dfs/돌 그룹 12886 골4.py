# 2024-01-27
# 돌 그룹 12866
# 골4

from collections import deque

a, b, c = map(int, input().strip().split(' '))

# 한 개는 완료된 상태이고 두 개가 남았을 때,  16, 29 -> 32 ,13 -> 19 26 -> 38 7 -> 31 14 -> 17 28 -> 34 11 -> 23 22 -> 1 44 -> 2 43 -> 4 41 -> 8 37  두 개가 반복 되면 끝

# x + x , y -x  , 전체 - (x+y)
# (전체) / 3 으로 만드는 방법은?

check = set()

dq = deque()
dq.append(tuple(sorted([a, b, c, ])))
check.add(tuple(sorted([a, b, c, ])))

while dq:
    x, y, z = dq.popleft()
    if x == y and y == z:
        print(1)
        exit(0)

    # case 1
    x1 = x + x
    y1 = y - x
    temp1 = tuple(sorted([x1, y1, z]))
    if temp1 not in check:
        dq.append(temp1)
        check.add(temp1)

    # case2
    x2 = x + x
    z2 = z - x
    temp2 = tuple(sorted([x2, y, z2]))
    if temp2 not in check:
        dq.append(temp2)
        check.add(temp2)

    # case3
    y3 = y + y
    z3 = z - y
    temp3 = tuple(sorted([x, y3, z3]))
    if temp3 not in check:
        dq.append(temp3)
        check.add(temp3)

print(0)
