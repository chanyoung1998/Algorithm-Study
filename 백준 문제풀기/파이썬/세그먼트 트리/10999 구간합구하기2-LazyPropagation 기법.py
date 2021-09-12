import sys
import math
# https://4legs-study.tistory.com/128
n,m,k = map(int,sys.stdin.readline().rstrip().split())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
x = math.ceil(math.log2(n))
seg =[0 for _ in range(2**(x+1))]
lazy = [0 for _ in range(2**(x+1))]


def build():
    for i in range(n):
        seg[i+2**x] = numbers[i]
    for i in range(2**x - 1,0,-1):
        seg[i] = seg[2*i] + seg[2*i+1]

    return


def update_lazy(node,nl,nr):

    if lazy[node] != 0:
        seg[node] += lazy[node] * (nr-nl + 1)
        if nl != nr:
            lazy[2 * node] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
        lazy[node] = 0

    return


# update_range query b-c구간에 d만큼 더하는 것
def update_range(node,nl,nr,b,c,d):

    update_lazy(node,nl,nr)
    # 완전히 벗엇나는 경우
    if nr < b or c < nl:
        return
    # 완전히 포함되는 경우
    if b <= nl and nr <= c:
        seg[node] += d * (nr-nl + 1)
        # 구간 노드라면 양쪽 자식에 lazy값을 추가
        if nl != nr:
            lazy[node*2] += d
            lazy[node*2 + 1] += d
        return

    # 걸치는 범위인 경우
    mid = (nl+nr) // 2
    update_range(2 * node, nl,mid,b,c,d)
    update_range(2 * node + 1,mid+1,nr,b,c,d)
    seg[node] = seg[node*2] + seg[node * 2 + 1]

    return


def subSub(node,nl,nr,b,c):
    update_lazy(node,nl,nr)

    if nr < b or c < nl:
        return 0

    if b <= nl and nr <= c:
        return seg[node]

    mid = (nl+nr) // 2
    return subSub(2*node,nl,mid,b,c) + subSub(2*node + 1,mid +1,nr,b,c)

build()
ret = []
for _ in range(m+k):
    query = list(map(int,sys.stdin.readline().rstrip().split()))

    if query[0] == 1:
        update_range(1,0,2**x - 1,query[1]-1,query[2]-1,query[3])

    else:
        ret.append(subSub(1,0,2**x - 1,query[1]-1,query[2]-1))

for i in ret:
    print(i)