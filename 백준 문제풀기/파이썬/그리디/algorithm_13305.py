'''
내용:백준 알고리즘 단계별 풀기 그리디 13305 주유소
날짜:21년2월12일
사용 언어:파이썬
'''
import sys
n = int(input())
distances = list(map(int,input().split()))
prices = list(map(int,input().split()))
cost = 0
min_price = sys.maxsize

for price,distance in zip(prices,distances):
    if price < min_price :
        min_price = price
    cost += min_price * distance


print(cost)