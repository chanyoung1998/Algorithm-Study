''' 
내용:백준 알고리즘 정렬 10989 카운팅 정렬
날짜:21년1월24일 
사용 언어:파이썬
'''
import sys

#이렇게 소스 코드를 작성하면 계속해서 메모리 초과 오류가 발생한다.
'''n = int(input())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array_count = [0]*n

for i in array:
        array_count[i] += 1

for i in range(n):
    if array_count[i] == 0:
        continue
    else:
        for j in range(array_count[i]):
            print(i)'''

n = int(input())
array_count = [0]* 10001

for i in range(n):
    num = int(sys.stdin.readline())
    array_count[num] += 1


for i in range(10001):
    if array_count[i] == 0:
        continue
    else:
        for j in range(array_count[i]):
            print(i)




    
    


    