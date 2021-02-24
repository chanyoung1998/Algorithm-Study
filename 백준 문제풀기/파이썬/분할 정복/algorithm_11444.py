'''
내용:백준 알고리즘 단계별 풀기 분할 정복 11444 피보나치수 6
날짜:21년2월24일
사용 언어:파이썬
'''
def power_matrix(a,b):
    ret = [[0 for _ in range(2)] for _ in range(2)]
    if b == 1:
        for i in range(2):
            for j in range(2):
                a[i][j] %= 1000000007
        return a
    elif b == 2:
        for i in range(2):
            for j in range(2):
                for w in range(2):
                    ret[i][j] += (a[i][w] * a[w][j]) % 1000000007
                    ret[i][j] %= 1000000007
        return ret

    temp = power_matrix(a, b // 2)
    for i in range(2):
        for j in range(2):
            for w in range(2):
                ret[i][j] += (temp[i][w] * temp[w][j]) % 1000000007
                ret[i][j] %= 1000000007
    if b % 2 == 0:
        return ret
    else:
        ret_ = [[0 for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for w in range(2):
                    ret_[i][j] += (ret[i][w] * a[w][j]) % 1000000007
                    ret_[i][j] %= 1000000007
        return ret_


def fibonacci_matrix(n):
    ret = power_matrix(a,n-1)
    print(ret[0][0])

n = int(input())
a = [[1,1],[1,0]]
if n == 1:
    print(1)
else:
    fibonacci_matrix(n)



# o(n)시간이 걸려서 시간 초과 발생, 행렬의 곱셈까지는 생각 했느나 거듭제곱을 이용해야 한다는 걸 생각 못함.
'''def fibonacci_matrix(n):
    if n == 0:
        return [[0]]
    elif n == 1:
        return [[1]]


    a = [[1, 0],[0, 1]]
    b = [[1] for _ in range(2)]
    ret = [[0 for _ in range(2)] for _ in range(2)]
    count = 0
    while count != n-1:
        for i in range(2):
            for j in range(1):
                for w in range(2):
                    ret[i][j] += a[i][w] * b[w][j] % 1000000007
                    ret[i][j] %= 1000000007
                    if i == 0 and j == 0 and w == 1:
                        a[1][0] = 0
                        a[1][0] += ret[i][j]

        ret[0][1] = a[0][0]
        ret[1][1] = ret[0][0]
        count += 1
        a = ret
        ret = [[0 for _ in range(2)] for _ in range(2)]

    return a

print(fibonacci_matrix(n)[0][0])'''