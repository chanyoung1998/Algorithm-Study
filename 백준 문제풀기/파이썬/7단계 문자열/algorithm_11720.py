''' 
내용:백준 알고리즘 단계별 풀기 문자열 11720 숫자의 합
날짜:21년1월10일 
사용 언어:파이썬
'''

n = int(input())

num_list = input()
sum = 0
for i in num_list:
    sum = sum+int(i)
print(sum)