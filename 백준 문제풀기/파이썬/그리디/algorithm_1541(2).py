expression = input().split('-')
sum = []

for exp in expression:
    e = exp.split('+')
    temp = 0
    for num in e:
        temp += int(num)
    sum.append(temp)

ret = 0
for i in range(len(sum)):
    if i == 0:
        ret += sum[i]
    else:
        ret -= sum[i]
print(ret)


