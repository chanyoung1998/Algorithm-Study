'''
내용:백준 알고리즘 단계별 풀기 for문 10950번 A+B-3
날짜:21년1월6일
사용 언어:파이썬
'''

num = int(input())

for i in range(num):
    inputlist = input().split()
    A = int(inputlist[0])
    B = int(inputlist[1])
    print(A+B)