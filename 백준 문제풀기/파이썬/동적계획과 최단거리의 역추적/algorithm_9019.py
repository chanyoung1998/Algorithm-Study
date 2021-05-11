'''
내용:백준 알고리즘 단계별 풀기 동적계획과 최단거리의 역추적 9019 DSLR
날짜:21년5월 11일
사용 언어:파이썬
'''
import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    path = [0 for _ in range(10000)]
    queue = deque()
    path[a] = -1
    queue.append(a)

    while queue:
        x = queue.popleft()
        if x == b:
            break
        for i in range(4):
            if i == 0:
                p = (2 * x) % 10000
                if path[p] == 0:
                    path[p] = ('D',x)
                    queue.append(p)
            elif i == 1:
                p = x - 1
                if x == 0:
                    p = 9999
                if path[p] == 0:
                    path[p] = ('S',x)
                    queue.append(p)
            elif i == 2:
                temp = str(x)
                if len(temp) != 4:
                    temp = '0' * (4-len(temp)) + temp
                if len(temp) > 1:
                    p = temp[1:] + temp[0]
                else:
                    p = temp
                p = int(p)
                if path[p] == 0:
                    path[p] = ('L',x)
                    queue.append(p)
            elif i == 3:
                temp = str(x)
                if len(temp) != 4:
                    temp = '0' * (4-len(temp)) + temp
                if len(temp) > 1:
                    p = temp[-1] + temp[:-1]
                else:
                    p = temp
                p = int(p)
                if path[p] == 0:
                    path[p] = ('R',x)
                    queue.append(p)
    temp = b
    ret = []
    while True:
        if temp == a:
            break
        ret.append(path[temp][0])
        temp = path[temp][1]

    for r in ret[::-1]:
        print(r,end='')
    print()

