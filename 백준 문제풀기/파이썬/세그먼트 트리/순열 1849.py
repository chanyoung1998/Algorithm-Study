#시간 초과 발생 및 재귀 한계 초과
import sys
import math
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
array = [0 for _ in range(n+1)]
x = math.ceil(math.log2(n))
segment = [0 for _ in range(2**(x+1))]
parent = [i for i in range(0,2**x)]
org = [0 for _ in range(n)]

for i in range(n):
    array[i+1] = int(sys.stdin.readline())
    segment[2**x + i] = 1


def init():

    for i in range(2**x - 1,0,-1):
        segment[i] = segment[2 * i] + segment[2 * i + 1]

    for i in range(2**x-1,n-1,-1):
        union(i,i-1)


def update(a):

    index = 2**x + a
    segment[index] = 0
    index //= 2
    while index >= 1:
        segment[index] = segment[2 * index] + segment[2 * index + 1]
        index //= 2


def subSum(index,l,r,target):

    if index >= 2**(x+1) or target == 0:
        return 0

    if segment[index] == target:

        return r

    if target < segment[index]:

        lc = index * 2
        rc = index * 2 + 1
        mid = (l+r)//2

        return max(subSum(lc,l,mid,target if target < segment[lc] else segment[lc] ), subSum(rc,mid+1,r, 0 if target < segment[lc] else target-segment[lc]))

def find(a):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a])

    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

init()
for i in range(1,n+1) :
    c = subSum(1, 0, 2 ** x - 1, array[i] + 1)
    #print('c:',c)
    p = find(c)
    #print("p:",p)
    update(p)
    if p != 0:
        union(p,p-1)
    org[p] = i

for i in org:
    print(i)
