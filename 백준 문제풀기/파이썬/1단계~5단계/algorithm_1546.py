'''
내용:백준 알고리즘 단계별 풀기 1차원 배열 1546번 평균
날짜:21년1월8일
사용 언어:파이썬
'''


n = int(input())
score_list = list(map(int,input().split()))
max_socre = max(score_list)

new_score_list = []

for i in score_list:
    new_score_list.append(i/max_socre*100)

print(sum(new_score_list)/len(new_score_list))


