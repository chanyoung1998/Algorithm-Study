from collections import deque


number,k = map(int,input().rstrip().split())
dp = [-1 for _ in range(1000001)]
m = len(list(str(number)))


dq = deque()
dq.append((number,0))
dp[number] = 0
ret = -1
while dq:
    cur,cnt = dq.popleft()
    if cnt == k:
        ret = max(ret,cur)
        continue

    nth = list(map(int,list(str(cur))))
    # print(nth)
    for i in range(m):
        for j in range(i+1,m):
            if not (nth[j] == 0 and i == 0):
                next = cur - nth[i] * 10**(m-1-i) - nth[j] * 10**(m-1-j) + nth[i] * 10**(m-1-j) + nth[j] * 10 **(m-1-i)
                if dp[next] != cnt + 1:
                    dp[next] = cnt + 1
                    dq.append((next,cnt+1))



print(ret)