import sys

n = int(sys.stdin.readline().rstrip())
base = [[3,2],[1,0]]
mod = 1000000007

def matrix_gop(a,b):
    answer = []
    for idx1 in range(len(a)):
        row = []
        for idx2 in range(len(b[0])):
            tmp = 0
            for idx3 in range(len(a[0])):
                tmp += (a[idx1][idx3] * b[idx3][idx2]) % mod
                tmp %= mod
            row.append(tmp)
        answer.append(row)
    return answer

def matrix_power(a,x):
    res = [[1,0],[0,1]]
    base = [[3,2],[1,0]]
    while x > 0:
        if x % 2 == 1:
            res = matrix_gop(base,a)
        x /= 2
        a = matrix_gop(a,a)

    return res

print(matrix_gop(matrix_power(base,n-4),[[3],[0]]))