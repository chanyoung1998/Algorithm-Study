'''
내용:백준 알고리즘 정렬 2108 통계학
날짜:21년1월24일
사용 언어:파이썬
'''
import sys

#문제 마이너스값에 대한 평균이 나왔을 때 반올림..?
def average(array):
    sum_array = sum(array)
    return sum_array/len(array)


def middle(array):
    array.sort()
    return array[len(array)//2]


#mode함수가 가장 오류가 많이난다. 1. 음수 값 처리 문제 절대값이 4000을 넘지 않는다.  array_count[value][0] += 1이 부분에서 계속 에러 발생 모든 값에 +1이 더해진다...
def mode(array):

    array_count = [[0,0]] * (abs(max(array))+1)

    for i in range(len(array)):
        value = array[i]
        if value >= 0:
            array_count[value][0] += 1
        else:
            array_count[abs(value)][1] += 1

    max_ = 0
    for i in range(len(array_count)):
        for j in range(0,2):
            if array_count[i][j] > max_:
                max_ = array_count[i][j]

    flag = 0 #부호
    index = 0
    k = 0 #최빈값이 여러개인 경우, 두 번째 최빈값 반환
    for i in range(len(array_count)):
        for j in range(0,2):
            if array_count[i][j] == max and k < 2:
                index = i
                flag = j
                k += 1


    if flag == 0:
        return index
    elif flag != 1:
        return -index


def diff_max_min(array):
    return max(array) - min(array)

n = int(input())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

print(int(round(average(array),1)))
print(middle(array))
print(mode(array))
print(diff_max_min(array))