'''
내용:백준 알고리즘 단계별 풀기 기본 수학 2869번 달팽이는 올라가고 싶다
날짜:21년1월11일
사용 언어:파이썬
'''

A,B,V = input().split()
A = int(A)
B = int(B)
V = int(V)

count_day = 0
displacement = 0
'''
이 방법이 맞는 지는 모르겠지만 시간 초과가 떠버린다
while displacement < V:
    displacement = displacement + A
    if displacement >= V :
        count_day = count_day + 1
        break
    displacement = displacement-B
    count_day = count_day + 1

print(count_day)
'''

count_day = (V-B)/(A-B)
if count_day == int(count_day):
    print(int(count_day))
else:
    print(int(count_day)+1)






