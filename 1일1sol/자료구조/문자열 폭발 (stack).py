
strings = list(input().rstrip())
explosion = list(input().rstrip())

stack = []
exidx = 0
ret = []
for i in range(len(strings)):

    if not stack:
        exidx = 0
        if strings[i] == explosion[exidx]:
            stack.append((i,exidx))
            exidx += 1
    else:
        top_i,top_exidx = stack[-1]
        if strings[i] == explosion[top_exidx+1]:
            stack.append((i,top_exidx+1))
            exidx = top_exidx + 2
        elif strings[i] == explosion[0]:
            stack.append((i,0))
            exidx = 1
        else:
            exidx = 0

    if exidx == len(explosion):
        for i in range(len(explosion)):
            ret.append(stack.pop()[0])

        exidx = 0

target = len(explosion)- 1
while stack:
    top_i,top_exidx = stack[-1]
    if target < 0:
        target = len(explosion) - 1

    if top_exidx == target:
        ret.append(stack.pop()[0])
        target -= 1

if len(ret) == len(strings):
    print("FRULA")
else:

    ret.sort()
    ridx = 0
    for i in range(len(strings)):
        if i == ret[ridx]:
            ridx+=1
            continue
        print(strings[i],end='')




