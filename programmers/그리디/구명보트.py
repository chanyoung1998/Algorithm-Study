from collections import deque
'''
24-08-11
프로그래머스
구명 보트
'''

def solution(people, limit):
    peopleOrderByASC =deque(sorted(people))


    cnt = 0
    while peopleOrderByASC:

        heavy = peopleOrderByASC.pop()

        if peopleOrderByASC and heavy + peopleOrderByASC[-1] <= limit:
            peopleOrderByASC.pop()
            cnt += 1
        elif peopleOrderByASC and heavy + peopleOrderByASC[0] <= limit:
            peopleOrderByASC.popleft()
            cnt += 1
        else:
            cnt += 1


    return cnt

assert solution([70, 50, 80, 50],100) == 3
