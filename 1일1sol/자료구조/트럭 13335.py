'''
24 03 14
자료구조
큐
수학
구현
'''
import sys
from collections import deque

N,L,W = map(int,sys.stdin.readline().split(' '))
trucks = list(map(int,sys.stdin.readline().split(' ')))
dq = deque()
curWeight = 0
time = 0

for i in range(N):
    while True:
        if len(dq) == L:
            popTruck = dq.popleft()
            curWeight -= popTruck

        if curWeight + trucks[i] <= W:
            break
        else:
            dq.append(0) # 투명 트럭

        time += 1


    curWeight += trucks[i]
    dq.append(trucks[i])
    time += 1

print(time+L)