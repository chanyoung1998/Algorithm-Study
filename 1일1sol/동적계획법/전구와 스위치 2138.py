import sys
import copy

N = int(sys.stdin.readline())

initial = list(map(int,list(sys.stdin.readline().strip())))
target = list(map(int,list(sys.stdin.readline().strip())))




def lightOn(light, x):

    if x == 0:
        light[x] = (light[x]+1) % 2
        light[x+1] = (light[x+1]+1) % 2

    elif x == N-1:
        light[x] = (light[x]+1) % 2
        light[x-1] = (light[x-1]+1) % 2

    else:
        light[x-1] = (light[x-1]+1) % 2
        light[x] = (light[x]+1) % 2
        light[x+1] = (light[x+1]+1) % 2

tmp = copy.copy(initial)
cnt = 1
flag = True
lightOn(tmp,0)
for i in range(1,N):
    if tmp[i-1] != target[i-1]:
        lightOn(tmp,i)
        cnt += 1

for i in range(N):
    if tmp[i] != target[i]:
        flag = False
        break


tmp2 = copy.copy(initial)
cnt2 = 0
flag2 = True
for i in range(1, N):
    if tmp2[i - 1] != target[i - 1]:
        lightOn(tmp2, i)
        cnt2 += 1

for i in range(N):
    if tmp2[i] != target[i]:
        flag2 = False
        break

if flag and flag2:
    print(min(cnt,cnt2))
elif flag:
    print(cnt)
elif flag2:
    print(cnt2)
else:
    print(-1)
