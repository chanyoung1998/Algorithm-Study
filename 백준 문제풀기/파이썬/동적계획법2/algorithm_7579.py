'''
내용:백준 알고리즘 단계별 풀기 동적 계획법 7579 앱
날짜:21년3월11일
사용 언어:파이썬
'''

import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
memory = list(map(int,sys.stdin.readline().split()))
costs = list(map(int,sys.stdin.readline().split()))

dp_m = deque([0,memory[0]])
dp_c = deque([0,costs[0]])
min = sys.maxsize
i = 1
while i != N:
    pop_memory = dp_m.popleft()
    pop_cost = dp_c.popleft()

    if pop_memory + memory[i] >= M:
        if min > pop_cost + costs[i]:
            min = pop_cost + costs[i]
    else:
        dp_m.append(pop_memory)
        dp_c.append(pop_cost)


if N == 1:
    print(costs[0])
else:
    print(min)



