''' 
내용:백준 알고리즘 단계별 풀기 문자열 1152 단어의 개수 
날짜:21년1월10일 
사용 언어:파이썬
'''

s_1 = input().strip()
s = s_1.split(' ')

if s == ['']:
    print(0)
else:
    print(len(s))
