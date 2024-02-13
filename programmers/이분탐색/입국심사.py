import sys

def solution(n, times):
    answer = 0

    lo = 0
    hi = sys.maxsize

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        cnt = check(mid,times)

        if cnt < n:
            lo = mid
        else:
            hi = mid

    return hi


    return answer


# x시간 동안 검사할 수 있는 사람의 수
def check(x,times):

    cnt = 0
    for t in times:
        cnt += x // t

    return cnt

print(solution(6,[7,10]))