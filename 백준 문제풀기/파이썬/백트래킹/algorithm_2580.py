import sys

'''inputs = [[0, 3, 5, 4, 6, 9, 2, 7, 8],
[7, 8, 2, 1, 0, 5, 6, 0, 9],
[0, 6, 0, 2, 7, 8, 1, 3, 5],
[3, 2, 1, 0, 4, 6, 8, 9, 7],
[8, 0, 4, 9, 1, 3, 5, 0, 6],
[5, 9, 6, 8, 2, 0, 4, 1, 3],
[9, 1, 7, 6, 5, 2, 0, 8, 0],
[6, 0, 3, 7, 0, 1, 9, 5, 2],
[2, 5, 8, 3, 9, 4, 7, 6, 0]]'''
inputs = []
blanks = []

for i in range(9):
    inputs.append(list(map(int,input().split(' '))))

for i in range(9):
    for j in range(9):
        if inputs[i][j] == 0:
            blanks.append([i,j])

#blank[cnt]에 들어갈 숫자를 결정하는 함수(dfs)
def Sdoku(cnt):
    if cnt == len(blanks):
        for input in inputs:
            print(*input)
        sys.exit()
        return
    blank_x = blanks[cnt][0] #blank의 행
    blank_y = blanks[cnt][1] #blank의 열

    for i in range(1,10):
        if determine(blank_x,blank_y,i):
            inputs[blank_x][blank_y] = i
            Sdoku(cnt+1)
            inputs[blank_x][blank_y] = 0


#input[i][j]에 k가 들어갈 수 있나?
def determine(i,j,k):
    #가로줄 확인,세로줄 확인
    temp = []
    for s in range(9):
        if k == inputs[i][s] or k == inputs[s][j]:
            return False
    #3*3안에 있는 지 확인
    for s1 in range(i//3*3,i//3*3+3):
        for s2 in range(j//3*3,j//3*3+3):
            if k == inputs[s1][s2]:
                return False

    return True

Sdoku(0)




