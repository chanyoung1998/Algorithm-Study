import sys

n = int(sys.stdin.readline())
cows = []
for _ in range(n):
    cows.append(tuple(map(int,sys.stdin.readline().rstrip().split())))
cows.sort()
# print(cows)
r = sys.maxsize
for i in range(n-1):
    if cows[i][1] == 1 and cows[i+1][1] == 0:
        r = min(r,cows[i+1][0]-cows[i][0]-1)

    elif cows[i][1] == 0 and cows[i+1][1] == 1:
        r = min(r, cows[i + 1][0] - cows[i][0]-1)

if r != sys.maxsize:
    cnt = 1
    end = cows[0][0]
    for i in range(1,n):
        if cows[i][1] == 1:
            if cows[i][0] <= end+r:
                end = cows[i][0]
            else:
                cnt += 1
                end = cows[i][0]
    print(cnt)
else:
    if cows[0][1] == 0:
        print(0)
    else:
        print(1)


