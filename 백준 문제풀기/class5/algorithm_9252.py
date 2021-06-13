import sys

string1 = sys.stdin.readline().rstrip()
string2 = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(string1)+1)] for _ in range(len(string2)+1)]

for i in range(1,len(string2)+1):
    for j in range(1,len(string1)+1):
        if string2[i-1] == string1[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

max_length = dp[len(string2)][len(string1)]


x = len(string2)
y = len(string1)

ret = []
while dp[x][y] != 0:
    if string1[y-1] == string2[x-1]:
       ret.append(string1[y-1])
       x -= 1
       y -= 1
    else:
        if dp[x-1][y] > dp[x][y-1]:
            x = x-1
        else:
            y = y-1

print(max_length)
for i in ret[::-1]:
    print(i,end='')