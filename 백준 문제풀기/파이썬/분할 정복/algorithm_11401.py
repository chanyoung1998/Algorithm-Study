'''
내용:백준 알고리즘 단계별 풀기 분할 정복 11401 이항계수 3
날짜:21년2월23일
사용 언어:파이썬
'''
def power(a,n,c):
    if n == 0:
        return 1
    x = power(a, n //2, c)

    if n % 2 == 0:
        return x * x % c
    else:
        return x * x * a % c


n, k = map(int, input().split())
p = 1000000007

fact =[1 for _ in range(n+1)]

for i in range(2,n+1):
    fact[i] = fact[i-1] * i % p

A = fact[n]
B = (fact[n-k] * fact[k]) % p
print((A % p) * (power(B, p-2, p) % p) % p)




'''mam = [[-1 for i in range(k+1)] for j in range(n+1)]


def comb(n,k):

    if n == 0 or k == 0 or n == k:
        mam[n][k] = 1
        return 1

    if mam[n][k] != -1:
        return mam[n][k] % 1000000007
    else:
        mam[n][k] = comb(n-1,k) +comb(n-1,k-1)
    return mam[n][k] % 1000000007



comb(n,k)
print(mam[n][k] % 1000000007)'''