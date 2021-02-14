'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 2004 조합 0의 개수
날짜:21년2월14일
사용 언어:파이썬
풀이 참고 :1.  https://www.crocus.co.kr/407
          2.   https://jaimemin.tistory.com/908
'''


def fiveCount(num):
    count = 0
    i = 5
    while num//i >= 1:
        count += num//i
        i *= 5
    return count


def twoCount(num):
    count = 0
    i = 2
    while num//i >= 1:
        count += num//i
        i *= 2
    return count

n, k = map(int,input().split())
m = n - k
five = fiveCount(n) - (fiveCount(k)+fiveCount(m))
two = twoCount(n) - (twoCount(k)+twoCount(m))
print(min(five,two))

