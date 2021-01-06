'''
내용:백준 알고리즘 단계별 풀기 for문 111021 A+B-7
날짜:21년1월6일
사용 언어:파이썬

input.split()함수의 반환값은 리스트이다.
print함수에서 기본적으로 구분자 "," 는 띄어쓰기 한 칸인데 sep = ''으로 설정하면 띄어쓰기를 안 하게 설정 할 수 있다.  그리고  end = 값도 설정 가능 하다.
'''

n = int(input())
list = []

for i in range(n):
    list.append(input().split())

for i in range(n):
    A = int(list[i][0])
    B = int(list[i][1])
    print('Case #',i+1,': ',A+B,sep='')



