import heapq
from collections import deque
n,k = map(int,input().split())
number = (input())
stack = []

i = k

for idx,num in enumerate(number):

    while stack and i > 0 and stack[-1] < num:
        stack.pop()
        i -= 1

    stack.append(num)

# 반례
# 7 3
# 7654321
while stack and i > 0:
    i -= 1
    stack.pop()

print(''.join(stack))


