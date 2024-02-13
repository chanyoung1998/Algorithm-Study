def solution(n, lost, reserve):
    answer = 0
    reserve.sort()

    lost_student = [False for _ in range(n + 2)]
    for l in lost:
        lost_student[l] = True

    for r in reserve:
        if lost_student[r]:
            lost_student[r] = False

    reserve = list(set(reserve) - set(lost))
    lost.sort()

    for r in reserve:
        if lost_student[r - 1]:
            lost_student[r - 1] = False
        elif lost_student[r + 1]:
            lost_student[r + 1] = False

    return n - sum(lost_student[1:-1])

