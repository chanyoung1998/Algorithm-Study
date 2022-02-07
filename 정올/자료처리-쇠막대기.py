import sys

inputs = list(sys.stdin.readline().rstrip())
stack = []

line = [0 for _ in range(len(inputs)+1)]
cnt = 0
for i in range(len(inputs)):
    if inputs[i] == '(':
        stack.append(i)
    else:
        pop = stack.pop()
        if pop + 1 == i:
            cnt += len(stack)
            # laser
        else:
            
            cnt+=1 #자르기전 스틱의 총 개수 더해주기 위해
            # stick

print(cnt)