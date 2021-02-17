from collections import deque
import sys


def push(queue, x):
    queue.append(x)


def pop(queue):
    if empty(queue) == 1:
        print(-1)
        return
    print(queue.popleft())


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

    if cmd[0] == 'push':
        push(queue, int(cmd[1]))

    elif cmd[0] == 'pop':
        pop(queue)

    elif cmd[0] == 'size':
        size(queue)
    elif cmd[0] == 'empty':
        print(empty(queue))
    elif cmd[0] == 'front':
        front(queue)
    elif cmd[0] == 'back':
        back(queue)