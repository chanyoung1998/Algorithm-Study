'''
내용:백준 알고리즘 정렬  10814 나이순 정렬
날짜:21년1월25일
사용 언어:파이썬
'''

n = int(input())
info = []

for i in range(n):
    inputs = input().split(' ')
    age = int(inputs[0])
    name = inputs[1]
    info.append([age,name])

info.sort(key = lambda x: x[0])
for i in info:
    print(i[0],i[1])
