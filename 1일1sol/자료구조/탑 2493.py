import sys

n = int(sys.stdin.readline())
height = list(map(int,sys.stdin.readline().strip().split(' ')))
stack = []
ret = [0 for _ in range(n)]

for i in range(n):
    if stack:
        current = height[i]
        while stack and height[stack[-1]] <= height[i]:
            popIndex = stack.pop()

        if stack:
            ret[i] = stack[-1] + 1
        stack.append(i)
    else:
        stack.append(i)


print(*ret)