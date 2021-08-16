import sys

#bottom - up gogogo
n = int(sys.stdin.readline().rstrip())
life = list(map(int,sys.stdin.readline().rstrip().split()))
life.sort(reverse=True)

dp = [[[0 for _ in range(61)] for _ in range(61)]for _ in range(61)]

for i in range(0,61):
    for j in range(i,61):
        for k in range(j,61):
            if i == 0 and j == 0:
                dp[k][0][0] = k // 9 + 1 if k % 9 != 0 else k // 9

            elif i == 0:
                new_k = k-9 if k-9 > 0 else 0
                new_j = j-3 if j-3 > 0 else 0
                if new_j > new_k:
                    new_j,new_k = new_k,new_j
                dp[k][j][i] = dp[new_k][new_j][i] + 1

                new_k = k - 3 if k - 3 > 0 else 0
                new_j = j - 9 if j - 9 > 0 else 0
                if new_j > new_k:
                    new_j, new_k = new_k, new_j
                dp[k][j][i] = min(dp[k][j][i],dp[new_k][new_j][i]+1)

            else:
                new_k = k - 9 if k-9 > 0 else 0
                new_j = j - 3 if j-3 > 0 else 0
                new_i = i - 1 if i-1 > 0 else 0

                temp = sorted([new_k,new_j,new_i],reverse=True)
                dp[k][j][i] = dp[temp[0]][temp[1]][temp[2]] + 1

                new_k = k - 9 if k - 9 > 0 else 0
                new_j = j - 1 if j - 1 > 0 else 0
                new_i = i - 3 if i - 3 > 0 else 0

                temp = sorted([new_k,new_j,new_i],reverse=True)
                dp[k][j][i] = min(dp[k][j][i],dp[temp[0]][temp[1]][temp[2]]+1)

                new_k = k - 1 if k - 1 > 0 else 0
                new_j = j - 9 if j - 9 > 0 else 0
                new_i = i - 3 if i - 3 > 0 else 0

                temp = sorted([new_k,new_j,new_i],reverse=True)
                dp[k][j][i] = min(dp[k][j][i], dp[temp[0]][temp[1]][temp[2]]+ 1)

                new_k = k - 1 if k - 1 > 0 else 0
                new_j = j - 3 if j - 3 > 0 else 0
                new_i = i - 9 if i - 9 > 0 else 0

                temp = sorted([new_k,new_j,new_i],reverse=True)
                dp[k][j][i] = min(dp[k][j][i], dp[temp[0]][temp[1]][temp[2]]+ 1)

                new_k = k - 3 if k - 3 > 0 else 0
                new_j = j - 1 if j - 1 > 0 else 0
                new_i = i - 9 if i - 9 > 0 else 0

                temp = sorted([new_k,new_j,new_i],reverse=True)
                dp[k][j][i] = min(dp[k][j][i], dp[temp[0]][temp[1]][temp[2]]+ 1)

                new_k = k - 3 if k - 3 > 0 else 0
                new_j = j - 9 if j - 9 > 0 else 0
                new_i = i - 1 if i - 1 > 0 else 0

                temp = sorted([new_k,new_j,new_i],reverse=True)
                dp[k][j][i] = min(dp[k][j][i], dp[temp[0]][temp[1]][temp[2]]+ 1)

if len(life) == 3:
    print(dp[life[0]][life[1]][life[2]])
elif len(life) == 2:
    print(dp[life[0]][life[1]][0])
elif len(life) == 1:
    print(dp[life[0]][0][0])

'''

top-down 방식

dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]


def attack(hp_1, hp_2=0, hp_3=0):
    if hp_1 < 0:
        hp_1 = 0
    if hp_2 < 0:
        hp_2 = 0
    if hp_3 < 0:
        hp_3 = 0

    if hp_1 == 0 and hp_2 == 0 and hp_3 == 0:
        return 0

    if dp[hp_1][hp_2][hp_3] != 0:
        return dp[hp_1][hp_2][hp_3]

    a = attack(hp_1 - 9, hp_2 - 3, hp_3 - 1)
    b = attack(hp_1 - 9, hp_2 - 1, hp_3 - 3)
    c = attack(hp_1 - 3, hp_2 - 9, hp_3 - 1)
    d = attack(hp_1 - 3, hp_2 - 1, hp_3 - 9)
    e = attack(hp_1 - 1, hp_2 - 9, hp_3 - 3)
    f = attack(hp_1 - 1, hp_2 - 3, hp_3 - 9)

    dp[hp_1][hp_2][hp_3] = min(a, b, c, d, e, f) + 1

    return dp[hp_1][hp_2][hp_3]


scv_cnt = int(input())
line = input()
scv_hps = [int(hp) for hp in line.split()]

print(attack(*scv_hps))


'''