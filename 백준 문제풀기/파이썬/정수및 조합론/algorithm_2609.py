'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 2609
날짜:21년2월13일
사용 언어:파이썬
'''

n, m = map(int, input().split())
min_value = min(n, m)
G = 1
i = 1
for i in range(min_value, 0, -1):
    if n % i == 0 and m % i == 0:
        G *= i
        n //= i
        m //= i
        break

print(G)
print(G * n * m)




