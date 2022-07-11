import sys
# https://beginthread.tistory.com/18

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

check_row = [False for _ in range(n)]
check_col = [False for _ in range(n)]

totoal_jewely = 0
total_rock = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            totoal_jewely += 1
        elif board[i][j] == 1:
            total_rock += 1
def check(s_x,s_y,e_x,e_y):
    cnt_jewely = 0
    cnt_rock = 0
    for i in range(s_x,e_x+1):
        for j in range(s_y,e_y+1):
            if board[i][j] == 1:
                cnt_rock += 1
            elif board[i][j] == 2:
                cnt_jewely += 1

    return (cnt_jewely, cnt_rock)


#dir = 0이면 가로 방향
#dir = 1이면 세로 방향
def divide(s_x,s_y,e_x,e_y,dir,l):

    jewely, rock = check(s_x,s_y,e_x,e_y)
    # print(jewely,rock)
    # print(l,':',s_x,s_y,e_x,e_y,dir)
    if jewely == 0:
        return 0 #잘못 자른 경우

    elif jewely == 1 and rock == 0:
        return 1

    ans = 0


    if dir == 0:
        # 세로로 자를예정
        for i in range(s_x,e_x+1):
            for j in range(s_y,e_y+1):
                if board[i][j] == 1:
                    flag = 0
                    for k in range(s_x,e_x+1):
                        if board[k][j] == 2:
                            flag = 1
                            break

                    if flag == 1:
                        continue
                    temp1 = divide(s_x, s_y, e_x, j-1,1,l+f'{i}{j}{1} ')
                    if temp1 == 0:
                        continue
                    temp2 = divide(s_x, j+1, e_x, e_y,1,l+f'{i}{j}{1} ')
                    ans += temp1*temp2
    elif dir == 1:

        #가로로 자를예정
        for i in range(s_x,e_x+1):
            for j in range(s_y,e_y+1):
                if board[i][j] == 1:

                    flag = 0
                    for k in range(s_y, e_y + 1):
                        if board[i][k] == 2:
                            flag = 1
                            break

                    if flag == 1:
                        continue

                    temp1 =  divide(s_x, s_y,i-1, e_y,0,l+f'{i}{j}{0} ')
                    if temp1 == 0:
                        continue
                    temp2 = divide(i+1, s_y, e_x, e_y,0,l+f'{i}{j}{0} ')
                    ans +=temp1 * temp2




    return ans


ans = divide(0,0,n-1,n-1,1,'') + divide(0,0,n-1,n-1,0,'')
if ans == 0:
    print(-1)
else:
    print(ans)



