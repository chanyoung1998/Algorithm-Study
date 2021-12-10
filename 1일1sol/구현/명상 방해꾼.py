import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
birds = []
birds_2 =[]
for _ in range(n):
    inputs = sys.stdin.readline().rstrip()
    birds.append(inputs[0])
    birds_2.append(list(map(int,inputs[2:])))

'''ret_bird = 0
ret_center = sys.maxsize
#i번 째 새를 잡는다.
for i in range(n):
    center = 0
    max_center = 0
    for j in range(m):
        for k in range(n):
            if k == i:
                continue
            if birds[k] == 'L':
                center -= birds_2[k][j]
            else:
                center += birds_2[k][j]

        max_center = max(max_center,abs(center))

    #print(max_center)
    if max_center < ret_center:
        ret_center = max_center
        ret_bird = i

print(ret_bird+1)
print(ret_center)
'''

center = [0 for _ in range(m)]
for i in range(m):
    c = 0
    for j in range(n):
        if birds[j] == 'L':
            c -= birds_2[j][i]
        else:
            c +=  birds_2[j][i]
    center[i] = c

#print(center)

ret_bird = 0
ret_center = sys.maxsize

#i 번째 새를 잡을 때
for i in range(n):
    c = 0
    ret_c = 0

    if birds[i] == 'L':
        for j in range(m):
            c += (center[j] + birds_2[i][j])
            ret_c = max(abs(c), ret_c)
    else:
        for j in range(m):
            c += (center[j] - birds_2[i][j])
            ret_c = max(abs(c),ret_c)

    if ret_c < ret_center:
        ret_center = ret_c
        ret_bird = i


print(ret_bird+1)
print(ret_center)
