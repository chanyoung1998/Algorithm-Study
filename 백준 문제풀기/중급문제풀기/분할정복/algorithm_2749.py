import sys

n = int(sys.stdin.readline())
mod = 1000000
matrix =[[1,1],[1,0]]
def matrix_power(matrix,x):

    answer =[[1,0],[0,1]]

    while x > 0:
        if x % 2 == 1:
            answer = matrix_mul(answer,matrix)
        matrix = matrix_mul(matrix,matrix)
        x = x//2

    return answer


def matrix_mul(matrixA,matrixB):
    answer = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixA[0])):
                answer[i][j] += matrixA[i][k] * matrixB[k][j] % mod
                answer[i][j] %= mod
    return answer

print(matrix_mul(matrix_power(matrix,n-1),[[1],[0]])[0][0])


'''
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
'''




