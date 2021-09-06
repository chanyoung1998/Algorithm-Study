#파이썬으로 시간초과 안나올라면 query에서 아예 update를 하면서 찾아야한다

import sys
import math
def init(node,start,end):
    if start==end:
        tree[node]=1
        return 1

    mid=(start+end)//2
    tree[node]=init(node*2,start,mid)+init(node*2+1,mid+1,end)
    return tree[node]

def query(node,start,end,val):
    #update하는 부분
    tree[node]-=1

    if start==end:
        return start
    mid = (start + end) // 2
    if tree[node*2]>=val:
        return query(node*2,start,mid,val)
    return query(node*2+1,mid+1,end,val-tree[node*2])

N=int(input())
size=2**(math.ceil(math.log(N,2))+1)
tree=[0 for i in range(size)]
L=[0 for i in range(N+1)]
init(1,1,N)

for i in range(1,N+1):
    indx=query(1,1,N,int(sys.stdin.readline().rstrip())+1)
    L[indx]=i

for i in range(1,N+1):
    print(L[i])