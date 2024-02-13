
from collections import deque

# 틀린 풀이
def solution(N, number):
    queue = deque()
    queue.append((N,1))

    numSet = set()
    numSet.add(N)
    i = 1
    while queue:

        curNumber, count = queue.popleft()

        if curNumber == number or count > 8:
            if count > 8:
                return -1
            else:
                return count

        if i < count:
            queue.append((int(str(N)*count),count))
            numSet.add(int(str(N)*count))
            i += 1

        a = curNumber * N
        b = curNumber + N
        c = curNumber // N
        d = N // curNumber
        e = curNumber - N
        f = N - curNumber

        candidate = [a, b, c, d, e, f]
        for cand in candidate:
            if cand >= 1 and cand not in numSet:
                numSet.add(cand)
                queue.append((cand, count + 1))


# 맞은 풀이
def solution2(N,number):

    numberSets = dict()
    numberSets[1] = set([N])
    for i in range(2,9):
        numberSets[i] = set([int(str(N) * i)])

    for i in range(1,9):
        for j in range(1,i):
            x = numberSets[j]
            y = numberSets[i-j]
            for numX in x:
                for numY in y:
                    numberSets[i].add(numX+numY)
                    numberSets[i].add(numX-numY)
                    numberSets[i].add(numX*numY)
                    if numY != 0:
                        numberSets[i].add(numX//numY)

    count = 1
    for numberSet in numberSets.values():
        for x in numberSet:
            if x == number:
                return count

        count += 1

    return -1




print(solution2(5,12))
print(solution2(2,11))







# 4시 25분
# 5 , 1 => 5
# 5 , 2 => 5/5 = 1, 5+5=>0, 5*5=25, 5-5=0 , 55 = 55
# 5 , 3 =>