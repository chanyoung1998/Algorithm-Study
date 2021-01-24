''' 
내용:백준 알고리즘 정렬 2750번 수 정렬하기
날짜:21년1월24일 
사용 언어:파이썬
'''

n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list.sort()
for i in (num_list):
    print(i)