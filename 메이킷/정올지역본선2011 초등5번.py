import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
v = [(1,1)]
for _ in range(k):
    v.append(tuple(map(int,sys.stdin.readline().rstrip().split())))
v.append((1,1))
l = int(sys.stdin.readline().rstrip())
cnt = 0
for i in range(1,k+2):
    x = v[i-1][0]
    y = v[i][0]
    if x > y:
        x,y = y,x

    if x <= l and l < y:
        cnt += 1

answer = [0 for _ in range(cnt+1)]
pos = 0

for i in range(1,k+2):
    x = v[i-1][0]
    y = v[i][0]
    if x > y:
        x,y = y,x

    if x <= l and l < y:
        pos += 1
        if v[i-1][0] < v[i][0]:
            answer[pos-1] += abs(v[i-1][0]-l) * 2 + 1
            answer[pos] += abs(v[i][0]-l-1) * 2 + 1
        else:
            answer[pos - 1] += abs(v[i - 1][0] - l-1) * 2 + 1
            answer[pos] += abs(v[i][0] - l) * 2 + 1

    else:
        if x == y:
            answer[pos] += abs(v[i-1][1]-v[i][1]) * 2
        else:
            answer[pos] += abs(v[i-1][0]-v[i][0]) * 2

answer[0] += answer[cnt]
print(max(answer)//2)
