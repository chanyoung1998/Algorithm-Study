import sys

n = int(sys.stdin.readline())
augmented_matrix = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
#print(augmented_matrix)




'''for i in range(1,n):
    a = (augmented_matrix[0][0] / augmented_matrix[i][0])
    for j in range(len(augmented_matrix[i])):
        augmented_matrix[i][j] = augmented_matrix[0][j] - a * augmented_matrix[i][j]


for i in range(2,n):
    a = (augmented_matrix[1][1] / augmented_matrix[i][1])
    for j in range(len(augmented_matrix[i])):
        augmented_matrix[i][j] = augmented_matrix[1][j] - a * augmented_matrix[i][j]
'''

for k in range(1,n):
    for i in range(k, n):
        a = (augmented_matrix[k-1][k-1] / augmented_matrix[i][k-1])
        for j in range(len(augmented_matrix[i])):
            augmented_matrix[i][j] = augmented_matrix[k-1][j] - a * augmented_matrix[i][j]

#print(augmented_matrix)

for k in range(n-2,-1,-1):
    for i in range(k, -1,-1):
        if augmented_matrix[i][k+1] == 0:
            continue
        a = (augmented_matrix[k+1][k+1] / augmented_matrix[i][k+1])
        for j in range(len(augmented_matrix[i])):
            augmented_matrix[i][j] = augmented_matrix[k+1][j] - a * augmented_matrix[i][j]
#print(augmented_matrix)

for i in range(n):
    print(int(round(augmented_matrix[i][n]/augmented_matrix[i][i],1)),end=' ')

'''
for i in range(1,-1,-1):
    a = (augmented_matrix[2][2] / augmented_matrix[i][2])
    for j in range(len(augmented_matrix[i])):
        augmented_matrix[i][j] = augmented_matrix[2][j] - a * augmented_matrix[i][j]
    '''
