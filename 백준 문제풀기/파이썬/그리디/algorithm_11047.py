'''
내용:백준 알고리즘 단계별 풀기 그리디 11047 거스름돈
날짜:21년1월27일
사용 언어:파이썬
'''

n, k = map(int,input().split(' '))
coin = []
change = 0
for i in range(n):
    coin.append(int(input()))

i = len(coin)-1
while k > 0:
    if k >= coin[i]:
        change += k//coin[i]
        k %= coin[i]
    i -= 1
print(change)