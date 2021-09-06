import sys
import math
n,m,k = map(int,sys.stdin.readline().rstrip().split())
x = math.ceil(math.log2(n))
segment_tree = [0 for _ in range(2**(x+1))]
number = [0 for _ in range(n)]
for i in range(n):
    input = int(sys.stdin.readline())
    segment_tree[i+2**x] = input
    number[i] = input
for i in range((2**x)-1,0,-1):
    segment_tree[i] = segment_tree[2*i] + segment_tree[2*i + 1]


def update(b,c):
    index = 2**x + b
    segment_tree[index] = c
    index //= 2
    while index >= 1:
        segment_tree[index] = segment_tree[2*index] + segment_tree[2*index + 1]
        index //= 2



def prefix_sum(index,l,r,target_l,target_r):

    if r < target_l or target_r < l:
        return 0

    if target_l <= l and r <= target_r:
        return segment_tree[index]

    lc_index = index * 2
    rc_index = index * 2 + 1
    mid = (l+r) // 2
    return prefix_sum(lc_index,l,mid,target_l,target_r) + prefix_sum(rc_index,mid+1,r,target_l,target_r)

for _ in range(m+k):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())

    if a == 1:
        update(b-1,c)
    elif a == 2:
        print(prefix_sum(1,0,2**x-1,b-1,c-1))