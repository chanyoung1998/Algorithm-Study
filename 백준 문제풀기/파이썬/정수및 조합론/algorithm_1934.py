'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 1934
날짜:21년2월13일
사용 언어:파이썬
'''
def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

n = int(input())
inputs = []
for i in range(n):
    inputs.append(list(map(int, input().split())))

for inp in inputs:
    n = inp[0]
    m = inp[1]
    G = GCD(n, m)
    print(n*m//G)




