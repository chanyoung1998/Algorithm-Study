'''
내용:백준 알고리즘 단계별 풀기 큐 5430 AC
날짜:21년2월18일
사용 언어:파이썬
'''
import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    cmds = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = deque((sys.stdin.readline().rstrip())[1:-1].split(','))
    flag = False
    reverse = False
    for cmd in cmds:
        if cmd == 'R' and not reverse:
            reverse = True
        elif cmd == 'R' and reverse:
            reverse = False
        elif cmd == 'D':
            if len(arr) == 0 or arr == deque(['']):
                flag = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if flag:
        print('error')
    elif arr == deque(['']):
        print([])
    else:
        if reverse:
            arr.reverse()
        print('[',end='')
        for i,data in enumerate(arr):
            if i == len(arr)-1:
                print(data,end='')
            else:
                print(data+',',end='')
        print(']')