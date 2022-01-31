import sys


n = int(sys.stdin.readline().rstrip())
heights = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
stack = []
result = [0 for _ in range(n)]

for i in range(n):

    if stack:
        if stack[-1][1] >= heights[i]:
            stack.append((i,heights[i]))
        else:
            while stack and stack[-1][1] < heights[i]:
                index,height = stack[-1]
                result[index] = i+1
                stack.pop()
            stack.append((i,heights[i]))



    else:
        stack.append((i,heights[i]))

for _ in range(n):
    print(result[_])


