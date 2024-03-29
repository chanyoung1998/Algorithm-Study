import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split(' '))
visit = set()
dq = deque()
dq.append((n, 0))
visit.add(n)

while dq:
    dist, time = dq.popleft()

    if dist == k:
        print(time)
        break


    a = dist * 2
    b = dist - 1
    c = dist + 1

    if a not in visit and a <= 100000:
        dq.append((a, time))
        visit.add(a)

    if b not in visit and b <= 100000:
        dq.append((b, time + 1))
        visit.add(b)

    if c not in visit and c <= 100000:
        dq.append((c, time + 1))
        visit.add(c)
