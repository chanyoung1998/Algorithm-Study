import sys
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(5)]
numberss = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(5)]
check = [[0,0,0,0,0] for _ in range(5)]

def sol():
    count = 0
    for i in range(5):
        if sum(check[i][0:]) == 5:
            count += 1
        if sum([check[0][i],check[1][i],check[2][i],check[3][i],check[4][i]]) == 5:
            count += 1

    s1 = 0
    s2 = 0
    for i in range(5):
        if check[i][i] == 1:
            s1 += 1
        if check[i][4-i] == 1:
            s2 += 1
    if s1 == 5:
        count+=1
    if s2 == 5:
        count += 1

    return count >= 3

ret = 0
for numbers in numberss:
    for number in numbers:
        flag = False
        for i in range(5):
            if flag:
                break
            for j in range(5):
                if board[i][j] == number:
                    check[i][j] = 1
                    ret += 1
                    if sol():
                        print(ret)
                        exit(1)
                    flag = True
                    break


