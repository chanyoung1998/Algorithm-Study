'''
내용:백준 알고리즘 단계별 풀기 for문 11022번 A+B-8
날짜:21년1월6일
사용 언어:파이썬
'''

n = int(input())
list = []

for i in range(n):
    list.append(input().split())


for i in range(n):
    A = int(list[i][0])
    B = int(list[i][1])
    print('Case #',i+1,': ',A,' ','+ ',B,' ','= ',A+B,sep='')
