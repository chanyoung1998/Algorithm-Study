'''
내용:백준 알고리즘 단계별 풀기 while문 10952번 A+B-5
날짜:21년1월6일
사용 언어:파이썬
'''

input_list = []
i = 0
while True:
    input_list.append(list(map(int,input().split())))
    if input_list[i][0] == 0 and input_list[i][1] == 0:
        break
    i = i+1

for j in range(0,i):
    print(input_list[j][0]+input_list[j][1])


