'''
24 03 22
오아시스 재결합
3015
플5
자료구조, 스택
'''
import sys

def bound(stack,target):
    low = 0
    high = len(stack)

    while low + 1 < high:
        mid = (low+high) // 2

        if stack[mid] > target:
            low = mid
        else:
            high = mid


    return low



n = int(sys.stdin.readline())
heights = []
for _ in range(n):
    heights.append(int(sys.stdin.readline()))

stack = []
ret  = 0
for i in range(n):
    if stack:
        cur = heights[i]
        if stack[-1] >= cur:
            stack.append(cur)
        else:
            popCount = 0
            while stack and stack[-1] < cur:
                pop = stack.pop()
                ret += len(stack) - bound(stack,pop) # pop이랑 - 현재 stack에 있는 애들이랑 쌍
                popCount += 1

            ret += popCount # cur랑 pop 쌍
            stack.append(cur)

    else:
        stack.append(heights[i])



while stack:
    pop = stack.pop()
    ret += len(stack) - bound(stack, pop)


print(ret)