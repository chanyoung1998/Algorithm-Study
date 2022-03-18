import sys
import math
from collections import deque

def transform_to_coord(p):

    tmp = int(math.sqrt(p*12 -3))
    n = (tmp-(tmp*tmp == p *12-3) +9) // 6
    n -= 1
    k = 3 * n * (n + 1) + 1 - p

    return (int(n),int(k))
def get_p(n,k):
    if n == 0: return 1
    k = (k+6*n) %(6*n)
    return (3* n *(n+1) + 1 - k)

def get_adj_node(n,k):

    if n == 0:
        return [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)]

    e = (k // n) if n != 0 else 0

    if k % n:
        adjlist = [(n,k-1),(n,k+1),(n+1,k+e),(n+1,k+e+1),(n-1,k-e),(n-1,k-e-1)]
    else:
        adjlist = [(n,k-1),(n,k+1),(n+1,k+e),(n+1,k+e+1),(n+1,k+e-1),(n-1,k-e)]

    return adjlist

a,b = map(int,sys.stdin.readline().rstrip().split())
start_x,start_y = transform_to_coord(a)
end_x,end_y = transform_to_coord(b)
dq = deque()
dq.append((a))
path = [-1 for _ in range(1000001)]
path[a] = 0
while dq:
    p = dq.popleft()
    n,k = transform_to_coord(p)

    if n == end_x and k == end_y:
        break

    e = (k // n) if n != 0 else 0

    if n == 0:
        adjlist = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)]
    elif k % n:
        adjlist = [(n, k - 1), (n, k + 1), (n + 1, k + e), (n + 1, k + e + 1), (n - 1, k - e), (n - 1, k - e - 1)]
    else:
        adjlist = [(n, k - 1), (n, k + 1), (n + 1, k + e), (n + 1, k + e + 1), (n + 1, k + e - 1), (n - 1, k - e)]

    for i,j in adjlist:
        if i < 0:
            continue
        q = get_p(i,j)
        if q > 1000000:
            continue
        if path[q] == -1:
            dq.append(q)
            path[q] = p

ret = []
while path[b] != 0:
    ret.append(int(b))
    b = path[b]
ret.append(a)

print(*ret[::-1])





