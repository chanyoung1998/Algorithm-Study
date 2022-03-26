import sys
n = int(sys.stdin.readline())
operations = list(sys.stdin.readline().rstrip().split())

stack = []

for i in range(n):
    if operations[i].isdigit():
        stack.append(operations[i])
    else:
        if operations[i] == '/':
            operations[i] = '//'
        A = stack.pop()
        B = stack.pop()
        ret = B + operations[i] + A
        stack.append(str(eval(ret)))

print(stack[0])