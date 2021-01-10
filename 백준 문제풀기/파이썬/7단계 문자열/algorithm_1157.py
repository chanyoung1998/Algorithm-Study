''' 
내용:백준 알고리즘 단계별 풀기 문자열 1157 단어공부
날짜:21년1월10일 
사용 언어:파이썬
'''



S = str(input()).lower()
count_list = []

for _ in range(26):
    count_list.append(0)

for s in S:
    index = ord(s)-ord('a')
    count_list[index] = count_list[index] +1

max = max(count_list)
count = 0 

for i in range(26):
    if count_list[i] == max:
        count = count + 1
    if count >=2:
        break

if count >= 2:
    print('?')
else:
    alphabet = chr(count_list.index(max)+ord('a'))
    print(alphabet.upper())

