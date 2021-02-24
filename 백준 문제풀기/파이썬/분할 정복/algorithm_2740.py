'''
내용:백준 알고리즘 단계별 풀기 분할 정복 2740 행렬 곱샘
날짜:21년2월23일
사용 언어:파이썬
'''

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int,input().split())
b = [list(map(int, input().split())) for _ in range(m)]
ret = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for w in range(m):
            ret[i][j] += a[i][w] * b[w][j]
for r in ret:
    print(*r)



