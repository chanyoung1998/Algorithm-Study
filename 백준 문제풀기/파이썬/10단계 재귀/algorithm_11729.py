'''
내용:백준 알고리즘 단계별 풀기 재귀단계 11729 하노이 탑 이동 순서
날짜:21년1월18일
사용 언어:파이썬
'''



def hanoi(n,start,by,dest):
    if n ==1:
        print(start,dest)
    else:
        hanoi(n-1, start,dest,by)
        print(start,dest)
        hanoi(n- 1, by,start, dest)




n = int(input())
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n,1,2,3)


