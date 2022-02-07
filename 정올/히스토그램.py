# https://loosie.tistory.com/305
# 스택 ,분할정복, 세그먼트
import sys


n = int(sys.stdin.readline())
inputs = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# inputs = list(map(int,sys.stdin.readline().rstrip().split()))
heights = inputs

stack = []
ret = 0
for i in range(len(inputs)):

    if stack:
        if heights[stack[-1]] <= heights[i]:
            stack.append(i)
        else:
            while stack and heights[stack[-1]] > heights[i]:
                pop = stack.pop()
                height = heights[pop]
                width = i
                if stack:
                    width = i - 1 - stack[-1]
                ret = max(ret,height * width)
            stack.append(i)
    else:
        stack.append(i)

while stack:
    pop = stack.pop()
    height = heights[pop]
    width = len(inputs)
    if stack:
        width = len(inputs)-1-stack[-1]
    ret = max(ret,width*height)
print(ret)