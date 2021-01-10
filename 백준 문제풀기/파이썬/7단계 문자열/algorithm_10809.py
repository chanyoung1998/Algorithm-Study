''' 
내용:백준 알고리즘 단계별 풀기 문자열 10809 알파벳 찾기
날짜:21년1월10일 
사용 언어:파이썬



************************************************************************************************
find 함수와 index 함수의 비교:

find 함수는 문자열에서만 사용 가능한 함수이다. 이와 유사한 기능을 하는 함수로 index 함수가 있다. index 함수는 문자열뿐만 아니라 리스트, 튜플과 같은 반복 가능한 iterable 자료형에서도 찾는 문자의 인덱스를 반환하는 함수로 쓰인다. find 함수와 다른 점은 find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력하지만 index함수는 >AttributeError가 발생한다.

출차:https://ooyoung.tistory.com/68

************************************************************************************************

'''

S = input()
alphabet = [-1] * 26


for s in S:
    index = ord(s) - ord('a')
    order = S.index(s)
    if alphabet[index] == -1:
        alphabet[index] = order
    else:
        continue
        
for i in range(26):
    print(alphabet[i],' ',sep = '',end= '')
    
    
'''
**find()함수 사용

word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 


'''
        