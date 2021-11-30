import sys
from itertools import permutations

def solution(n,weak,dist):

    m = len(dist)
    k = len(weak)
    ret = 100
    for i in range(k):
        weak.append(weak[i] + n)

    for start in range(k):
        for new_dist in permutations(dist,m):
            count = 1
            position = weak[start] + new_dist[count - 1]

            for index in range(start, start + k):
                if position < weak[index]:
                    count += 1
                    if count > m:
                        break
                    position = weak[index] + new_dist[count - 1]

            ret = min(ret, count)

    if ret > m:
        return -1
    else:
        return ret

print(solution(12,[1,3,4,9,10],[3]))


