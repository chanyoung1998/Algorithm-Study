import sys
from itertools import permutations

n,k = map(int,sys.stdin.readline().strip().split(' '))
kits =list(map(int,sys.stdin.readline().strip().split(' ')))
ret = 0
for permut in permutations(kits):
    total = 500
    flag = True
    for kit in permut:
        total += kit
        total -= k

        if total < 500:
            flag = False
            break

    if flag:
        ret += 1

print(ret)