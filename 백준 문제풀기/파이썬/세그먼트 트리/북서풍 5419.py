import sys
import math


def Subsum(index,l,r,target_l,target_r):

    if r < target_l or target_r < l:
        return 0

    if target_l <= l and r <= target_r:
        return segment[index]

    lc_index = index * 2
    rc_index = index * 2 + 1
    mid = (l+r) // 2
    return Subsum(lc_index,l,mid,target_l,target_r) + Subsum(rc_index,mid+1,r,target_l,target_r)


def update(a):

    index = 2**x + a
    segment[index] += 1
    index //= 2

    while index >= 1:
        segment[index] = segment[2 * index] + segment[2 * index + 1]
        index //= 2

    return

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    coord = []
    coord_y = []
    for i in range(n):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        coord.append((x,y))
        coord_y.append(y)

    coord_y = set(coord_y)
    coord_y = list(coord_y)
    coord_y.sort()

    index_y = dict()
    for i in range(len(coord_y)):
        index_y[coord_y[i]] = i
    x = math.ceil(math.log2(len(coord_y)))
    segment = [0 for _ in range(2**(x+1))]

    coord.sort(key=lambda x:(x[0],-x[1]))
    ret = 0
    for _,y in coord:
        index = index_y[y]
        ret += Subsum(1,0,2**x - 1,index,2**x-1)
        update(index)

    print(ret)

