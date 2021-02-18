'''
내용:백준 알고리즘 단계별 풀기 큐 1021 회전하는 큐
날짜:21년2월14일
사용 언어:파이썬
'''
from collections import deque
import math
n, m = map(int,input().split())
target = list(map(int,input().split()))
deq = deque(range(1,n+1))
count = 0 # 1번 연산 횟수
#op =2 이면 2번 연산, 3이면 3번 연산
ret = 0
while count != m:
    [distance, op] = [deq.index(target[count]),2] if deq.index(target[count]) < len(deq) - deq.index(target[count]) else [len(deq) - deq.index(target[count]),3]
    ret += distance
    if op == 2:
        for i in range(distance):
            '''deq.append(deq[0])
            deq.popleft()'''
            deq.rotate(-1)
        deq.popleft()
        count += 1

    elif op == 3:
        for i in range(distance):
            '''deq.appendleft(deq[-1])
            deq.pop()'''
            deq.rotate(1)
        deq.popleft()
        count += 1

print(ret)
