import sys

n = int(sys.stdin.readline().rstrip())
heights = list(map(int,sys.stdin.readline().rstrip().split()))
result = [0 for _ in range(n)]
stack = []


for i in range(n-1,-1,-1):

    if stack:
        if stack[-1][1] >= heights[i]:
            stack.append((i,heights[i]))
        else:
            while stack and stack[-1][1] < heights[i]:
                pop_index,pop_height = stack.pop()
                result[pop_index] = i+1

            stack.append((i,heights[i]))

    else:
        stack.append((i,heights[i]))


print(*result)