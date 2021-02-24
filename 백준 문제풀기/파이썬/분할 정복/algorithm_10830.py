'''
내용:백준 알고리즘 단계별 풀기 분할 정복 10830 행렬 거듭제곱
날짜:21년2월24일
사용 언어:파이썬
'''
n, b = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def power_matrix(a,b):
    ret = [[0 for _ in range(n)] for _ in range(n)]
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    elif b == 2:
        for i in range(n):
            for j in range(n):
                for w in range(n):
                    ret[i][j] += (a[i][w] * a[w][j]) % 1000
                    ret[i][j] %= 1000
        return ret

    temp = power_matrix(a, b // 2)
    for i in range(n):
        for j in range(n):
            for w in range(n):
                ret[i][j] += (temp[i][w] * temp[w][j]) % 1000
                ret[i][j] %= 1000
    if b % 2 == 0:
        return ret
    else:
        ret_ = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for w in range(n):
                    ret_[i][j] += (ret[i][w] * a[w][j]) % 1000
                    ret_[i][j] %= 1000
        return ret_


sol = power_matrix(a,b)
for s in sol:
    print(*s)