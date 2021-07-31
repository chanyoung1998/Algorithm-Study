import sys
string = sys.stdin.readline().strip()
length = len(string)
map = [[0 for _ in range(length)]for _ in range(length)]

for i in range(length):
    map[i][i] = 1
for i in range(length-1):
    if string[i] == string[i+1]:
        map[i][i+1] = 1

for i in range(3,length+1):
    for j in range(length-i+1):
        if string[j] == string[j + i - 1] and map[j+1][j + i - 2] == 1:
            map[j][j + i - 1] = 1


dp = [sys.maxsize for _ in range(length)]
dp[0] = 1
for i in range(1,length):
    for j in range(i+1):
        if j == 0 and map[j][i] == 1:
            dp[i] = 1
            break
        elif map[j][i] == 1:
            dp[i] = min(dp[i],1 + dp[j-1])

print(dp[-1])