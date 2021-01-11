'''
내용:백준 알고리즘 단계별 풀기 기본 수학 1712번 손익분기점
날짜:21년1월11일
사용 언어:파이썬
'''

inputlist= list(map(int,input().split()))
A = inputlist[0]
B = inputlist[1]
C = inputlist[2]

if C <= B :
    print('-1')
else:
    print(int(A/(C-B))+1)
