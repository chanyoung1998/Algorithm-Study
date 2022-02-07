import sys

n = int(sys.stdin.readline().rstrip())
inputs = list(sys.stdin.readline().rstrip())

red = []
blue = []
r = 0
b = 0

if inputs[0] == 'R':
    r = 1
else:
    b = 1


for i in range(1,n):
    if inputs[i] == inputs[i-1]:
        if inputs[i] == 'R':
            r += 1
        else:
            b += 1
    else:
        if inputs[i] == 'R':
            r = 1
            blue.append(b)
            b = 0
        else:
            b = 1
            red.append(r)
            r = 0

if r != 0:
    red.append(r)
elif b!= 0:
    blue.append(b)

if inputs[0] == inputs[-1]:
    if inputs[0] =='R':
        ret = min(sum(blue),sum(red[1:]),sum(red[:-1]))
    else:
        ret = min(sum(red),sum(blue[1:]),sum(blue[:-1]))
else:
    if inputs[0] == 'R':
        ret = min(sum(red[1:]), sum(blue[:-1]))
    else:
        ret = min(sum(blue[1:]), sum(red[:-1]))

print(ret)