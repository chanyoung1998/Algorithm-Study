'''
내용:백준 알고리즘 단계별 풀기 동적계획과 최단거리의 역추적 13913 숨바꼭질 4
날짜:21년5월 11일
사용 언어:파이썬
'''

import sys
from collections import deque
n, k = map(int,sys.stdin.readline().rstrip().split())
dp = [0 for _ in range(100001)]
path = [0 for _ in range(100001)]

path[n] = n

queue = deque()
queue.append(n)
dx = [1,-1,2]
while queue:
    x = queue.popleft()
    if x == k:
        break
    for i in dx:
        p = x + i
        if i == 2:
            p = 2 * x
        if 0 <= p <= 100000 and dp[p] == 0:
            dp[p] = dp[x] + 1
            path[p] = x
            queue.append(p)
print(dp[k])
ret = []
temp = k
while True:
    if temp == n:
        break
    ret.append(temp)
    temp = path[temp]
ret.append(n)
for i in ret[::-1]:
    print(i,end=' ')
