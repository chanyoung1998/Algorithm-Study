'''
내용:백준 알고리즘 단계별 풀기 for문 10871번 X보다 작은 수
날짜:21년1월6일
사용 언어:파이썬
'''

input_list = input().split()
N = int(input_list[0])
X = int(input_list[1])

A_list = input().split()

for i in range(N):
    if int(A_list[i]) < X:
        print(int(A_list[i]),end=' ')


'''
map함수는 리스트의 요소를 지정된 함수로 처리해주는 함수입니다.(map은 원본 리스트를 변경하지 않고 새로운 리스트를 생성합니다.)

list(map(함수,리스트))
tuple(map(함수,튜플))

>>> a = [1.2, 2.5, 3.7, 4.6]
>>> a = list(map(int, a))
>>> a
[1, 2, 3, 4]
'''