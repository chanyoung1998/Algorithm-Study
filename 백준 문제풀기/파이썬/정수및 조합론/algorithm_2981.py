'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 2981
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
    inputs.append(int(input()))
inputs.sort()
temp = []
for i in range(n-1):
    temp.append(inputs[i+1]-inputs[i])

gcd = temp[0]
for tp in temp:
    gcd = GCD(tp, gcd)


results = []
for i in range(2, int(gcd ** (1/2)) + 1):
    if(gcd % i == 0):
        results.append(i)
        if(gcd // i != i):
            results.append(gcd // i)
results.append(gcd)
results = sorted(set(results))

print(''.join([str(i) + ' ' for i in results])[:-1])
