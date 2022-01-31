import sys
from collections import deque
n,d,k,c = map(int,sys.stdin.readline().rstrip().split())
dq = deque()
check = [0 for _ in range(d+1)]
for _ in range(n):
    dq.append(int(sys.stdin.readline().rstrip()))

cnt = 1
check[c] = sys.maxsize
for i in range(k):
    if check[dq[i]] == 0:
        cnt += 1
    check[dq[i]] += 1
    # print(dq[i])

ret = cnt

for _ in range(n):

    pop = dq[0]
    dq.popleft()
    dq.append(pop)
    add = dq[k-1]

    if pop == add:
        continue

    check[pop] -= 1
    check[add] += 1

    if check[pop] == 0:
        cnt -= 1
    if check[add] == 1:
        cnt += 1



    ret = max(ret,cnt)


print(ret)



