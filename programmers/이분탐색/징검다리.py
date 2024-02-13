def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    low = 0
    high = distance + 1

    while low + 1 < high:
        mid = (low + high) // 2
        if sol(mid, rocks, n):
            low = mid
        else:
            high = mid

    return low


def sol(targetMinimumDistance, rocks, n):
    print(targetMinimumDistance,rocks,n)
    count = 0
    curPosition = 0

    j = 0
    while j < len(rocks) and count <= n:
        betweenDistance = rocks[j] - curPosition
        if betweenDistance < targetMinimumDistance:
            count += 1
        else:
            curPosition = rocks[j]

        j += 1

    if j == len(rocks) and count <= n:
        return True
    else:
        return False

print(solution(25,[2,14,11,21,17],2))




