import sys

n = int(sys.stdin.readline())
inputs = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
number = []

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i != j and i != k and j != k:
                number.append(int(str(i)+str(j)+str(k)))
# print(number)
# number = [324,328]
delete = []
for num in number:
    for target,s,b in inputs:
        target = str(target)
        num = str(num)
        s_ = 0
        b_ = 0
        for i in range(3):

            if target[i] == num[i]:
                s_ += 1
            elif target[i] == num[(i+1)%3] or target[i] == num[(i+2) %3]:
                b_ += 1

        if s != s_ or b != b_:
            delete.append(num)
            break

print(len(number) - len(delete))


