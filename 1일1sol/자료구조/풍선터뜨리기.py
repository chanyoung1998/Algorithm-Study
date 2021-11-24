import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
ballons = list(map(int,sys.stdin.readline().rstrip().split()))
dq = deque()
for i in range(n):
    dq.append((ballons[i],i+1))

while dq:
    data = dq[0][0]

    if data > 0:
        a,b = dq.popleft()
        dq.rotate(-a + 1)
        #print(dq)
        print(b,end=' ')
    else:
        a,b =dq.popleft()
        dq.rotate(-a)
        #print(dq)
        print(b,end=' ')
