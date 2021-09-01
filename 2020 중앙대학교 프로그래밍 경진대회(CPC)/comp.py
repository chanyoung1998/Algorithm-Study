from functools import cmp_to_key
import sys


n = int(sys.stdin.readline())
array = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]


def comp(x,y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1

    return 0

for x,y in sorted(array,key=cmp_to_key(comp)):
    print(x,y)