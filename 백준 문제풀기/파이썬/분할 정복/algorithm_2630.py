'''
내용:백준 알고리즘 단계별 풀기 분할 정복 2630 색종이접기
날짜:21년2월19일
사용 언어:파이썬
'''
import sys

def divide(arr,n,color):
    global count
    if n == 1:
        for ar in arr:
            for i in ar:
                if i == color:
                    count += 1
        return


    flag = True
    temp1 = arr[:n]
    new_arr = []
    for temp2 in temp1:
        temp3 = []
        for i in temp2[:n]:
            if i != color:
                flag = False
            temp3.append(i)
        new_arr.append(temp3)
    if flag:
        count += 1
    else:
        divide(new_arr, n//2,color)

    flag = True
    temp1 = arr[:n]
    new_arr = []
    for temp2 in temp1:
        temp3 = []
        for i in temp2[n:2*n]:
            if i != color:
                flag = False
            temp3.append(i)
        new_arr.append(temp3)
    if flag:
        count += 1
    else:
        divide(new_arr, n // 2,color)

    flag = True
    temp1 = arr[n:2*n]
    new_arr = []
    for temp2 in temp1:
        temp3 = []
        for i in temp2[:n]:
            if i != color:
                flag = False
            temp3.append(i)
        new_arr.append(temp3)
    if flag:
        count += 1
    else:
        divide(new_arr, n // 2,color)

    flag = True
    temp1 = arr[n:2*n]
    new_arr = []
    for temp2 in temp1:
        temp3 = []
        for i in temp2[n:2*n]:
            if i != color:
                flag = False
            temp3.append(i)
        new_arr.append(temp3)
    if flag:
        count += 1
    else:
        divide(new_arr, n // 2,color)


n = int(sys.stdin.readline())
arr = []
count = 0
flag_1 = True
flag_0 = True
for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    arr.append(temp)
    if 0 in temp:
        flag_1 = False
    if 1 in temp:
        flag_0 = False


if flag_0:
    print(count+1)
else:
    divide(arr, n // 2, 0)
    print(count)

count = 0
if flag_1:
    print(count+1)
else:
    divide(arr, n // 2, 1)
    print(count)