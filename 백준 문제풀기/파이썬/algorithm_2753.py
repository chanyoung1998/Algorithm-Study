'''
내용:백준 알고리즘 단계별 풀기 if문 2753번 윤년
날짜:21년1월6일
사용 언어:파이썬
'''

year = int(input())

if (year%4 == 0 and year%100 != 0) or year%400 ==0 :
    print('1')
else:
    print('0')
