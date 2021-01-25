'''
내용:백준 알고리즘 정렬  1427번 소트 인사이드
날짜:21년1월25일
사용 언어:파이썬
'''

n = str(input())
n = sorted(n,reverse=True)

for i in n:
    print(i,end='')