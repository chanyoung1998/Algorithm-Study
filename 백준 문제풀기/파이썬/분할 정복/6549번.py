'''
내용:백준 알고리즘 단계별 풀기 분할 정복 6549 히스토크램에서 가장 큰 직사각형
날짜:21년2월24일
사용 언어:파이썬
'''
import sys
sys.setrecursionlimit(10**6)


def sol(array,start,end):
    if start == end:
        return array[start]
    else:
        mid_index = (start+end)//2

        right_maxsize = sol(array,start,mid_index)
        left_maxsize = sol(array,mid_index+1,end)

        #겹치는 부분의 max_size 구하기
        nl = mid_index
        nr = mid_index + 1
        nh = min(array[nl],array[nr])
        tmp = 2 * nh

        cnt = 2
        while True:
            if (array[nl] == 0 or nl == start) and (array[nr] == 0 or nr == end):
                break
            elif array[nl] == 0 or nl == start:
                if array[nr + 1] < nh:
                    nh = array[nr + 1]
                nr += 1
            elif array[nr] == 0 or nr == end:
                if array[nl - 1] < nh:
                    nh = array[nl - 1]
                nl -= 1
            else:
                if array[nl - 1] > array[nr + 1]:
                    if array[nl - 1] < nh:
                        nh = array[nl - 1]
                    nl -= 1
                else:
                    if array[nr + 1] < nh:
                        nh = array[nr + 1]
                    nr += 1
            cnt += 1
            tmp = max(tmp, nh * cnt)

        return max(right_maxsize,left_maxsize,tmp)


while True:
    inputs = list(map(int,sys.stdin.readline().rstrip().split()))
    #print(inputs)
    if inputs == [0]:
        break
    n = inputs[0]
    array = inputs[1:]
    print(sol(array,0,n-1))


