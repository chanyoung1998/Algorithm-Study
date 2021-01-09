'''
내용:백준 알고리즘 단계별 풀기 1차원 배열 8958번 0X 퀴즈
날짜:21년1월8일
사용 언어:파이썬
'''

n = int(input())
ox_list = []


for i in range(n):
    ox_list.append(input())


score = 0
count = 1
for ox in ox_list:
    for str in ox:
        if(str=='x' or str =='X'):
            count = 1
        else:
            score = score + count
            count = count+1
    print(score)
    score = 0
    count = 1


