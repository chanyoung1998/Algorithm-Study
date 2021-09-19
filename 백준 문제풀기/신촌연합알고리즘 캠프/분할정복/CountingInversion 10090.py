import sys
import math
n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().rstrip().split()))
x = math.ceil(math.log2(n))
segment = [0 for _ in range(2**(x+1))]

def update(i):

    index = 2**x + i
    segment[index] = 1
    index //= 2

    while index >= 1:
        segment[index] = segment[2 * index] + segment[2 * index + 1]
        index //= 2

    return

def query(node,nl,nr,a,b):

    if b < nl or nr < a:
        return 0

    if a <= nl and nr <= b:
        return segment[node]

    mid = (nl+nr) // 2

    return query(2 * node,nl,mid,a,b) + query(2 * node + 1,mid + 1,nr,a,b)

ret = 0


for i in array:
    ret += query(1,0,2**x-1,i,2**x-1)
    update(i)
print(ret)