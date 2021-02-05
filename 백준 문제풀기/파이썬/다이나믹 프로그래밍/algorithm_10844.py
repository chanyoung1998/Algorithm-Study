'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  10844 쉬운 계단 수
날짜:21년2월5일
사용 언어:파이썬
'''

n = int(input())
x = [-1 for _ in range(n)]
count = 0

#x[length]에 들어갈 숫자 정하는 함수 x[0]가 가장 왼쪽에서 첫 번째 자리
#이 풀이는 시간 초과 발생한다
'''def dp(length):
    global count
    if length == n:
        count += 1
        return

    flag = 0
    for i in range(0,10):
        if length == 0 and i ==0:
            continue
        elif length == 0:
            x[length] = i
            dp(length+1)

        if flag >= 2:
            return

        if abs(x[length-1]-i) == 1 and length >= 1 :
            flag += 1
            x[length] = i
            dp(length+1)'''

#이전 풀이보단 빠르지만 n이 커지면 여젼히 시간 초과 발생
def dp(length):
    global count
    if length == n:
        print(*x)
        count += 1
        return

    if length == 0:
        for i in range(1,10):
            x[length] = i
            dp(length+1)
    else:
        if x[length-1] == 0:
            x[length] = 1
            dp(length+1)
        elif x[length-1] == 9:
            x[length] = 8
            dp(length+1)
        else:
            x[length] = x[length-1] - 1
            dp(length+1)
            x[length] = x[length-1] + 1
            dp(length+1)


dp(0)
print(count%1000000000)



