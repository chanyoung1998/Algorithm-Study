'''
내용:백준 알고리즘 단계별 풀기 브루트포스 1018 체스판
날짜:21년1월22일
사용 언어:파이썬
'''

n, m = map(int, input().split(' '))
listwb = []

for j in range(n):
    wb = input()
    listwb.append(wb)


def check_min(matrix):
    mis_block_b = 0
    # (0,0)이 black인 경우
    for i in range(8):
        for j in range(8):
            if ((i % 2 == 0) and (j % 2 == 0)) or ((i % 2 == 1) and (j % 2 == 1)):
                if matrix[i][j] != 'B':
                    mis_block_b += 1
            elif ((i % 2 == 1) and (j % 2 == 0)) or ((i % 2 == 0) and (j % 2) == 1):
                if matrix[i][j] != 'W':
                    mis_block_b += 1

    mis_block_w = 0
    # (0,0)이 white인 경우
    for i in range(8):
        for j in range(8):
            if ((i % 2 == 0) and (j % 2 == 0)) or ((i % 2 == 1) and (j % 2 == 1)):
                if matrix[i][j] != 'W':
                    mis_block_w += 1
            elif ((i % 2 == 1) and (j % 2 == 0)) or ((i % 2 == 0) and (j % 2) == 1):
                if matrix[i][j] != 'B':
                    mis_block_w += 1
    return min(mis_block_b, mis_block_w)


def sol():
    min_list = []
    for row in range(0, n - 7):
        for col in range(0, m - 7):
            matrix = [one_row[col:col + 8] for one_row in listwb[row:row + 8]]

            min_ = check_min(matrix)
            min_list.append(min_)

    return min(min_list)


print(sol())



