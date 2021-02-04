'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  1463 1로 만들기
날짜:21년2월4일
사용 언어:파이썬
'''
import sys

def dp(x, count):
    global min_count

    if x == 1:
        if count < min_count:
            min_count = count
        return


    for i in range(3):
        if x % 3 == 0 and i == 0:
            if mamo[x//3] != 0 :
                min_count = min(mamo[x//3]+1,min_count)
                continue
            dp(x // 3, count + 1)

        elif x % 2 == 0 and i == 1:
            if mamo[x//2] != 0 :
                min_count = min(mamo[x//2]+1,min_count)
                continue
            dp(x // 2, count + 1)

        elif i == 2:
            if mamo[x-1] != 0:
                min_count = min(mamo[x-1]+1,min_count)
                continue
            dp(x - 1, count + 1)

n = int(input())
mamo = [0 for _ in range(1000001)]
mamo[0] = 0
mamo[1] = 0
mamo[2] = 1
for i in range(3,n+1):
    min_count = sys.maxsize
    dp(i,0)
    mamo[i] = min_count

print(mamo[n])