'''
내용:백준 알고리즘 단계별 풀기 1차원 배열 2562번 최댓값
날짜:21년1월8일
사용 언어:파이썬
'''
array_list = []

for i in range(9):
    array_list.append(int(input()))

print(max(array_list))
print(array_list.index(max(array_list))+1)