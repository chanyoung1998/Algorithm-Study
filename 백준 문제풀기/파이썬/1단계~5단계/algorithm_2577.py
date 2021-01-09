'''
내용:백준 알고리즘 단계별 풀기 1차원 배열 2577번 숫자의 개수
날짜:21년1월8일
사용 언어:파이썬
'''


A = int(input())
B = int(input())
C = int(input())

DATA = str(A*B*C)
Count = [0,0,0,0,0,0,0,0,0,0]

for i in DATA:
    Count[int(i)] = Count[int(i)]+1

for i in Count:
    print(i)

'''
다른 방법 풀이  count함수 이용하기

a = int(input())
b = int(input())
c = int(input())

k = a*b*c
k_list = list(str(k))
for i in range(10):
    k_num_count = k_list.count(str(i))
    print(k_num_count)

'''
