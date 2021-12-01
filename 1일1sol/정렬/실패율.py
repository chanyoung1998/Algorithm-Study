def solution(n,stages):
    m = len(stages)
    failures = []



    for i in range(1,n+1):
        count = stages.count(i)
        if m == 0:
            failure = 0
        else:
            failure = count / m
        failures.append((i,failure))
        m -= count

    failures.sort(key=lambda x : (-x[1],x[0]))

    ret = []
    for i in range(n):
        ret.append(failures[i][0])
    return ret


solution(5,[2,1,2,6,2,4,3,3,3])