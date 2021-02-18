'''
내용:백준 알고리즘 단계별 풀기 큐 1966 프린터 큐
날짜:21년2월18일
사용 언어:파이썬
'''


import sys
from collections import deque
t = int(sys.stdin.readline().strip())
for i in range(t):
    n,m = map(int,sys.stdin.readline().strip().split())
    priority = map(int,sys.stdin.readline().strip().split())
    priority = deque(zip(priority,range(n)))
    count = 0
    index = -1
    while index != m:
        if priority[0][0] < max(priority)[0]:
            priority.append(priority[0])
            priority.popleft()
        else:
            index = priority[0][1]
            count += 1
            priority.popleft()

    print(count)







