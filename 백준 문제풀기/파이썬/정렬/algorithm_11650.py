'''
내용:백준 알고리즘 정렬  11650 좌표 정렬하기
날짜:21년1월25일
사용 언어:파이썬

https://dpdpwl.tistory.com/87
->람다식 활용하기
'''

n = int(input())
lists = []
for i in range(n):
    lists.append(list(map(int,input().split(' '))))
lists.sort(key = lambda x:(x[0],x[1]))

for i in lists:
    print(i[0],i[1])