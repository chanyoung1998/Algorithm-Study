''' 
내용:백준 알고리즘 단계별 풀기 문자열 1157 단어공부
날짜:21년1월10일 
사용 언어:파이썬

reverse 함수와 reversed함수의 차이점 공부하기
->  https://itholic.github.io/python-reverse-reversed/    <-

'''

s = input().split(' ')
s1 = s[0][::-1]
s2 = s[1][::-1]

'''
for i in s[0][::-1]:
    s1.append(i)
    
for i in s[1][::-1]:
    s2.append(i)
    
예를 들어 입력이 123 456이라면    
이렇게 하면 s1 = ['3','2','1'] s2=['6','5','4'] 이런 식으로 저장이 되어서 s1과 s2를 대소 비교하는게 힘들어진다.
'''

if s1 > s2:
    print(s1)
else:
    print(s2)







