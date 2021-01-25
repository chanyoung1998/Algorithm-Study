'''
내용:백준 알고리즘 정렬  11651 좌표 정렬하기2
날짜:21년1월25일
사용 언어:파이썬
'''

n = int(input())
lists = []
for i in range(n):
    lists.append(list(map(int,input().split(' '))))
lists.sort(key = lambda x:(x[1],x[0]))

for i in lists:
    print(i[0],i[1])