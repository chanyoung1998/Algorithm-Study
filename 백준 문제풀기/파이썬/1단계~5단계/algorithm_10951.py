'''
내용:백준 알고리즘 단계별 풀기 while문 10951번 A+B-4
입력이 끝날 때까지 입력을 받는 것 ,  EOF에 대해 알아 보세요.
날짜:21년1월6일
사용 언어:파이썬
'''

input_list = []

while True:
    try:
       input_list.append(list(map(int,input().split())))
    except EOFError:
        break;

for i in range(len(input_list)):
    print(input_list[i][0] + input_list[i][1])




