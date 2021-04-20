import sys
'''
ASDWADGFRQWE
GHASDQWE
'''
string1 = list(sys.stdin.readline().rstrip())
string2 = list(sys.stdin.readline().rstrip())
string2 = [' '] + string2
string1 = [' '] + string1
dp = [[0 for _ in range(len(string1))] for _ in range(len(string2))]
ret = ''

for i in range(1,len(string2)):
    for j in range(len(string1)):
        if string2[i] == string1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])


if dp[-1][-1] != 0:
    print(dp[-1][-1])
    target = dp[-1][-1]
    for temp in dp[::-1]:
        if target == 0:
            break


        target -= 1
    for i in ret[::-1]:
        print(i,end = '')
else:
    print(0)
