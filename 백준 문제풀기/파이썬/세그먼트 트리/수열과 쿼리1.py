import sys
import math
class Node:
    def __init__(self,index):
        self.index = index
        self.address = self


n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().rstrip().split()))
x = math.ceil(math.log2(n))
seg = [0 for _ in range(2**(x+1))]
origin = []
sorted_list = []
for i in range(n):
    origin.append(Node(i))
    sorted_list.append((array[i],origin[-1].address))

sorted_list.sort(key=lambda x:x[0])
#print('origin',origin)
#print('sorted',sorted_list)


def init():
    for i in range(n):
        seg[2**x + i] = 1
    for i in range(2**x - 1,0,-1):
        seg[i] = seg[2*i] + seg[2*i + 1]
    return
init()
#print('initseg',seg)
m = int(sys.stdin.readline())
#print('m',m)
query_list = [list(map(int,sys.stdin.readline().rstrip().split())) + [i] for i in range(m)]
query_list.sort(key=lambda x:x[2])
#print('query_list',query_list)

def update(a,k):

    for i in range(a,n):
        if sorted_list[i][0] <= k:
            #print('index:',sorted_list[i][1].index)
            index = 2**x + sorted_list[i][1].index
            seg[index] = 0
            index //= 2
            while index >= 1:
                seg[index] = seg[index * 2] + seg[index * 2 + 1]
                index //= 2
        else:
            a = i
            break

    return a


def Subsum(node,nl,nr,i,j):

    if nr < i or j < nl:
        return 0

    if i <= nl and nr <= j:
        return seg[node]
    mid = (nl+nr)//2
    return Subsum(2 * node,nl,mid,i,j) + Subsum(2 * node + 1,mid+1,nr,i,j)

a = 0
ret = []
for i,j,k,number in query_list:
    a = update(a,k)
    b = Subsum(1,0,2**x-1,i-1,j-1)
    #print(b)
    ret.append((number,b))

ret.sort(key=lambda x:x[0])
for i in range(len(ret)):
    print(ret[i][1])