import sys

'''n = int(sys.stdin.readline())
height = []'''
io = list(map(int,sys.stdin.readline().rstrip().split()))
n = io[0]
height = io[1:]
'''for _ in range(n):
    height.append(int(sys.stdin.readline()))
'''
stack = []
ret = 0

for i in range(n):
    while stack and height[stack[-1]] > height[i]:
        x = stack.pop()
        width = 0
        if not stack:
            width = i
        else:
            width = i - stack[-1] - 1

        ret = max(ret,height[x]*width)

    stack.append(i)

print(ret)