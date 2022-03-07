import sys
# 5
# 3 1 5 1
# 4 1 12 1
# 5 1 7 1
# 7 1 9 1
# 9 1 12 1

n = int(sys.stdin.readline().rstrip())
flower = []
for _ in range(n):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    if c*100+d <= 301 or a *100 + b == c*100 + d:
        continue
    flower.append((max(301,a*100+b),c*100+d))
flower.sort(key=lambda x:(x[0],-x[1]))

time = 301
#time 기준, time보다 이전이거나 같은 날에 핀 꽃 들 중 가장 오랫동안 피는 꽃 선택해야한다
i = 0
cnt = 0
while i < len(flower):

    tmpmax = time
    j = i
    while j < len(flower):
        if flower[j][0] <= time:
            tmpmax = max(tmpmax,flower[j][1])
            j += 1
        else:
            break

    if j == i:
        print(0)
        exit(0)

    if time < tmpmax:
        time = tmpmax
        cnt += 1

    if time >= 1201:
        break


    i = j


if time >= 1201:
    print(cnt)
else:
    print(0)