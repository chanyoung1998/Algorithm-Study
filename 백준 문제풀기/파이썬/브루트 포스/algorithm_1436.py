'''
내용:백준 알고리즘 단계별 풀기 브루트포스 1436 영화감독 숌
날짜:21년1월20일
사용 언어:파이썬
'''

n = int(input())
count = 0
i = 666

while count != n :
    str_i = str(i)
    if str_i.find('666') != -1:
        count += 1
    i += 1

print(str_i)



