import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

'''
# 1 Try

numbers.sort(reverse= True)

stack = []
ret = 0
for i in range(n):

    num = numbers[i]

    if stack:
        top = stack[-1]
        if top + num < top * num:
            stack.pop()
            ret += top * num
            continue

    stack.append(num)

for s in stack:
    ret += s
print(ret)
'''



plus = []
minus_zero = []
the_others = []
for i in range(n):
    if numbers[i] > 1:
        plus.append(numbers[i])
    elif numbers[i] < 1:
        minus_zero.append(numbers[i])
    else:
        the_others.append(numbers[i])

plus.sort(reverse=True)
minus_zero.sort()
ret = 0

for i in range(0,len(plus),2):
    if i+1< len(plus):
        ret += plus[i]*plus[i+1]
    else:
        ret += plus[i]

for i in range(0,len(minus_zero),2):
    if i+1 < len(minus_zero):
        ret += minus_zero[i]*minus_zero[i+1]
    else:
        ret += minus_zero[i]

ret += sum(the_others)

print(ret)

