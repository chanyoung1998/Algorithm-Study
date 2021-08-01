import sys

n = int(sys.stdin.readline().rstrip())
base = [[4,-1],[1,0]]
mod = 1000000007

def matrix_gop(a,b):

    answer = []
    for idx1 in range(len(a)):
        row = []
        for idx2 in range(len(b[0])):
            tmp = 0
            for idx3 in range(len(a[0])):
                tmp += (a[idx1][idx3] * b[idx3][idx2]) % mod
                tmp = (tmp+mod) % mod
            row.append(tmp)
        answer.append(row)


    return answer

def matrix_power(a,x):
    res = [[1,0],[0,1]]
    while x > 0:
        if x % 2 == 1:
            res = matrix_gop(res,a)
        a = matrix_gop(a,a)
        x = x // 2
    return res

if n % 2 == 1:
    print(0)
else:
    power = matrix_power(base,n//2)
    print(matrix_gop(power,[[1,0],[1,0]])[0][0])