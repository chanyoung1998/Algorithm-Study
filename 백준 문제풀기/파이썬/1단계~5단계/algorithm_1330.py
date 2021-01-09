'''
내용:백준 알고리즘 단계별 풀기 if문 1330번 두 수 비교하기
날짜:21년1월6일
사용 언어:파이썬
'''
num1,num2 = input().split(" ")
A =int(num1)
B =int(num2)
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

