'''
내용:백준 알고리즘 정렬  1181 단어 정렬
날짜:21년1월25일
사용 언어:파이썬
'''

n = int(input())
words = []

for i in range(n):
    word = input()
    if word not in words:
        words.append(word)
words.sort(key = lambda x : (len(x),x))
for i in words:
    print(i)
