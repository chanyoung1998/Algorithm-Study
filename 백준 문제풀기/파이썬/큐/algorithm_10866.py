'''
내용:백준 알고리즘 단계별 풀기 큐 10866 덱
날짜:21년2월18일
사용 언어:파이썬
'''

from collections import deque
import sys


def push_front(queue, x):
    queue.insert(0,x)


def push_back(queue, x):
    queue.append(x)


def pop_front(queue):
    if empty(queue) == 1:
        print(-1)
        return
    print(queue.popleft())


def pop_back(queue):
    if empty(queue) == 1:
        print(-1)
        return
    print(queue.pop())


def size(queue):
    print(len(queue))


def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0


def front(queue):
    if empty(queue) == 1:
        print(-1)
    else:
        print(queue[0])


def back(queue):
    if empty(queue) == 1:
        print(-1)
    else:
        print(queue[-1])


n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push_front':
        push_front(queue, int(cmd[1]))
    elif cmd[0] == 'push_back':
        push_back(queue, int(cmd[1]))
    elif cmd[0] == 'pop_front':
        pop_front(queue)
    elif cmd[0] == 'pop_back':
        pop_back(queue)
    elif cmd[0] == 'size':
        size(queue)
    elif cmd[0] == 'empty':
        print(empty(queue))
    elif cmd[0] == 'front':
        front(queue)
    elif cmd[0] == 'back':
        back(queue)