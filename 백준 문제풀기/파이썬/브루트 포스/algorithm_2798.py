'''
내용:백준 알고리즘 단계별 풀기 브루트포스 2798 블랙잭
날짜:21년1월18일
사용 언어:파이썬
'''

n,m = list(map(int,input().split(' ')))
card_num = list(map(int,input().split(' ')))

sum = 0
max = 0

for i in range(len(card_num)):
    for j in range(len(card_num)):
        for k in range(len(card_num)):
            if j == i or k ==i or j ==k:
                continue
            else:
                sum = card_num[i]+card_num[j]+card_num[k]
                if sum <= m and sum > max:
                    max = sum

print(max)