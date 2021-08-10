import sys
from collections import deque

s, t = map(int, sys.stdin.readline().rstrip().split())
check = set()

if s == t:
    print(0)
else:
    queue = deque()
    queue.append((s,''))
    find = -1
    while queue:
        x,ops = queue.popleft()
        if x == t:
            find = ops
            break
        if x > t and 1 in check:
            continue

        for i in range(3):
            if i == 0:
                if x * x not in check:
                    check.add(x*x)
                    queue.append((x*x,ops+'*'))
            elif i == 1:
                if x + x not in check:
                    check.add(x + x)
                    queue.append((x+x,ops+'+'))
            elif i == 2:
                if 1 not in check:
                    check.add(1)
                    queue.append((1,ops+'/'))
    print(find)