import sys



n = int(sys.stdin.readline().rstrip())
original = list(map(int,sys.stdin.readline().rstrip().split()))
target = list(map(int,sys.stdin.readline().rstrip().split()))
target_position = [0 for _ in range(n)]

for i in range(n):
    target_position[target[i]-1] = i

A = [target_position[v-1] for v in original]

cnt = 0
max_tmp = -1
for x in A:
    if x > max_tmp:
        max_tmp = x
        continue

    cnt += 1
print(cnt)


