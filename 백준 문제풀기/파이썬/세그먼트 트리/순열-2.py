#88%시간초과
import sys
import math

n = int(sys.stdin.readline())
array = [0 for _ in range(n+1)]
x = math.ceil(math.log2(n))
segment = [0 for _ in range(2**(x+1))]
org = [0 for _ in range(n)]

for i in range(n):
    array[i+1] = int(sys.stdin.readline())
    segment[2**x + i] = 1


def init():

    for i in range(2**x - 1,0,-1):
        segment[i] = segment[2 * i] + segment[2 * i + 1]


def update(a):

    index = 2**x + a
    segment[index] = 0
    index //= 2
    while index >= 1:
        segment[index] = segment[2 * index] + segment[2 * index + 1]
        index //= 2


def subSum(index,l,r,target):

    if l == r:
        return l
    lc = index * 2
    rc = index * 2 + 1
    mid = (l+r)//2

    if segment[lc] >= target:
        return subSum(lc,l,mid,target)
    else:
        return subSum(rc,mid+1,r,target-segment[lc])

init()
for i in range(1,n+1) :
    c = subSum(1, 0, 2 ** x - 1, array[i] + 1)
    update(c)
    org[c] = i

for i in org:
    print(i)