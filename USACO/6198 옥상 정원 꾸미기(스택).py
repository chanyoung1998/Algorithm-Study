import sys

n = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(n)]

stack = []

ret = 0
for i in range(n):
    if stack:
        if heights[stack[-1]] > heights[i]:
            stack.append(i)
        else:
            while stack and heights[stack[-1]] <= heights[i]:
                pop = stack.pop()
                ret += i - pop - 1
            stack.append(i)

    else:
        stack.append(i)

while stack:
    pop = stack.pop()
    ret += n - pop - 1
print(ret)