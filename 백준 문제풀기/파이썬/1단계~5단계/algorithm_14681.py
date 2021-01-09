'''
내용:백준 알고리즘 단계별 풀기 if문 14681번 사분면 고르기
날짜:21년1월6일
사용 언어:파이썬
'''

x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x<0 and y < 0 :
    print('3')
else:
    print('4')