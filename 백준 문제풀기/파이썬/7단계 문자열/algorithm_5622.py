''' 
내용:백준 알고리즘 단계별 풀기 문자열 5622 다이얼 
날짜:21년1월10일 
사용 언어:파이썬
'''

S = input()
dict = {('A','B','C'):2,('D','E','F'):3,('G','H','I'):4,('J','K','L'):5,('M','N','O'):6,
       ('P','Q','R','S'):7,('T','U','V'):8,('W','X','Y','Z'):9}
dict_keys = list(dict.keys())
dial_sec = [11,2,3,4,5,6,7,8,9,10]

count  = 0

for s in S:
    for dict_key in dict_keys:
        if s in dict_key:
            sec = dial_sec[dict[dict_key]]
            count = count +sec
            break

print(count)