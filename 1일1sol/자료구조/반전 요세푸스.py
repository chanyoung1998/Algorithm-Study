import sys
from collections import deque
n,k,m = map(int,sys.stdin.readline().rstrip().split())

dq = deque()

for i in range(1,n+1):
    dq.append(i)

cnt = 0
flag = 1

while dq:
    if cnt == m:
        flag = (flag + 1) % 2
        cnt = 0
    #순방향
    if flag == 1:
        for i in range(k-1):
            dq.append(dq.popleft())

        print(dq.popleft())
    #역방향
    else:
        for i in range(k-1):
            dq.appendleft(dq.pop())

        print(dq.pop())
    cnt += 1
