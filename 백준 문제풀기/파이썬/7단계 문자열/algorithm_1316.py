'''
내용:백준 알고리즘 단계별 풀기 문자열 1316 그룹 단어
날짜:21년1월10일
사용 언어:파이썬
'''

n = int(input())
word_list = []

for i in range(n):
    word_list.append(input())


count = len(word_list)
for word in word_list:
    for i in range(len(word)):
        if not(word.find(word[i],i+1) == -1 or word.find(word[i],i+1) == i+1):
            count = count -1
            break

print(count)