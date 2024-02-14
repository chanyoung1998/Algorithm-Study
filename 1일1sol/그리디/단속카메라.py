'''
2024 02 15
단속카메라
level3
그리디
'''

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))

    end = -30001

    for i in range(len(routes)):

        if end < routes[i][0]:
            answer += 1
            end = routes[i][1]

    return answer

