import sys

k = int(sys.stdin.readline().rstrip())
stack = []
for i in range(k):
    temp = int(sys.stdin.readline())
    if temp != 0:
        stack.append(temp)
    elif temp == 0:
        stack.pop(-1)

print(sum(stack))