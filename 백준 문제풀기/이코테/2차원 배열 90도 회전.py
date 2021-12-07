
def rotate_matrix_by_90_degree(matrix):
    row = len(matrix)
    column = len(matrix[0])
    ret = [[0 for _ in range(row)] for _ in range(column)]

    for r in range(row):
        for c in range(column):
            ret[c][row-r-1] = matrix[r][c]

    return ret

for a in rotate_matrix_by_90_degree([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]):
    print(*a)