import sys
import math
n,m,k = map(int,sys.stdin.readline().rstrip().split())
x = math.ceil(math.log2(n))
segment_tree = [0 for _ in range(2**(x+1))]
for i in range(n):
    segment_tree[i+2**x] = int(sys.stdin.readline())
for i in range(2**x-1,0,-1):
    segment_tree[i] = segment_tree[2*i] + segment_tree[2*i + 1]
print(segment_tree)
for _ in range(m+k):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())

