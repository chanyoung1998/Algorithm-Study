

# box 1~n안에 빵이 있을 때 , ith 박스 에서 x개 만큼의 빵을 i-1th 박스 로만 옮길 수 있을 때, 각 박스에 있는 방의 최대값이 최소가 되도록 빵을 옮기시오.
from copy import deepcopy
def solution(box):
    n = len(box)
    if n == 1 or box[0] >= max(box[1:]):
        return box[0]


    prevStatus = deepcopy(box)
    while True:

        last = n - 1
        start = n - 1
        flag = False
        while last > 0:
            sumBox = box[last]
            for i in range(last,0,-1):
                if box[i] >= box[i-1]:
                    sumBox += box[i-1]
                    start = i-1
                else:
                    break
            if last > start:
                boxesBetweenLS = (last-start)+1
                temp = start
                for i in range(start,start+(sumBox%boxesBetweenLS)):
                    box[i] = (sumBox) // boxesBetweenLS + 1
                    temp = i
                for i in range(start+(sumBox%boxesBetweenLS),last+1):
                    box[i] = sumBox // boxesBetweenLS

                last = temp

                flag = True
            else:

                last -= 1

        if prevStatus == box:
            break
        else:
            prevStatus = deepcopy(box)
        if not flag:
            break

    return max(box)
print(solution([1,5,7,6]))
