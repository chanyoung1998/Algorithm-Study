'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  1463 1로 만들기
날짜:21년2월4일
사용 언어:파이썬
'''
import sys
n = int(input())
count = 0
#그리디 알고리즘으로는 정답을 도출해 낼 수 없음 ex)10을 입력하면 4가 출력되어서
#틀리다. (10->5->4->2->1) 원래 정답은 3으로(10->9->3->1)
'''while n > 1:
    if n%3 == 0 :
        n = n//3
        count += 1
    elif n%2 == 0:
        n = n//2
        count += 1
    else :
        n = n -1
        count += 1
print(count)'''


min_count = sys.maxsize
#백트래킹 알고리즘을 사용하는 것은 시간 초과 오류가 난다
'''def dp(x,count):
    if x <= 1:
        global min_count
        if count < min_count:
            min_count = count
        return

    for i in range(3):
        if i ==0 and x % 3 ==0:
            dp(x//3,count+1)

        elif i == 1 and x % 2 == 0:
            dp(x//2,count+1)

        else:
            dp(x-1,count+1)

dp(n,count)
print(min_count)'''


