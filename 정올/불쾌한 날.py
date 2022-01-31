import sys

n = int(sys.stdin.readline().rstrip())
cows = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
stack = []
res = 0
for i in range(n):

    if stack:
        if stack[-1] > cows[i]:
            stack.append(cows[i])
        else:
            while stack and stack[-1] <= cows[i]:
                stack.pop()
            stack.append(cows[i])

    else:
        stack.append(cows[i])

    res += len(stack) - 1

print(res)
