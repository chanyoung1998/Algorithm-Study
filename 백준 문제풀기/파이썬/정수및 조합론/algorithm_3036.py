'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 3036 링
날짜:21년2월14일
사용 언어:파이썬
'''
def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

n = int(input())
radiuses = list(map(int,input().split()))
for i in range(1,n):
    g = GCD(radiuses[0],radiuses[i])
    print('{}/{}'.format(radiuses[0]//g, radiuses[i]//g))
