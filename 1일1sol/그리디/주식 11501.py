import sys
from collections import  deque, defaultdict
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    price =list(map(int,sys.stdin.readline().strip().split(' ')))
    maxPrice = deque(sorted(price,reverse=True))
    dict = defaultdict(int)
    for p in price:
        dict[p] += 1

    ret = 0
    for p in price:

        while dict[maxPrice[0]] == 0:
            maxPrice.popleft()

        if p != maxPrice[0]:
            ret += maxPrice[0] - p

        dict[p] -= 1

    print(ret)


