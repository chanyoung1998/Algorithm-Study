'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 5086
날짜:21년2월13일
사용 언어:파이썬
'''

inputs = []
while True:
    temp = list(map(int,input().split()))
    if temp == [0,0]:
        break
    else:
        inputs.append(temp)
for inp in inputs:
    if inp[1] % inp[0] == 0:
        print('factor')
    elif inp[0] % inp[1] == 0:
        print('multiple')
    else:
        print('neither')