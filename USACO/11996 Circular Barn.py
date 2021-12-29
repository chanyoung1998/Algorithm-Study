import sys
import copy
f = open("7.in","r")
n = int(f.readline().rstrip())
room = [int(f.readline().rstrip()) for _ in range(n)]
visit = [False for _ in range(n)]

sum = 0
lowest = sys.maxsize
lowestIndex = -1
for i in range(n):
    sum += room[i] -1
    if sum < lowest:
        lowest = sum
        lowestIndex = i

k = lowestIndex + 1
ans = 0
while True:
    done = True
    to = k
    for i in range(k,k+n):
        if room[i%n] == 0 and not visit[i%n]:
            to = i%n
            done = False

    if done:
        break

    fr = to
    dist = 0
    while True:
        if fr == -1:
            fr = n-1

        if room[fr] != 0 and not visit[fr]:
            break

        fr -= 1
        dist += 1

    ans += dist * dist
    visit[to] = True
    room[fr] -= 1



print(ans)

