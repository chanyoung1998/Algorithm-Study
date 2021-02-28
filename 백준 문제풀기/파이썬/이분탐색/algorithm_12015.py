import sys


def lower_bound(array, k):
    start = 0
    end = len(array)-1

    while start < end:
        mid = (start+end)//2

        if array[mid] >= k:
            end = mid
        else:
            start = mid + 1

    return end


n = int(input())
array = list(map(int,input().split()))
ret = [-sys.maxsize]
count = 0
x = 0
while x != len(array):

    if ret[-1] < array[x]:
        ret.append(array[x])
        count += 1
        x += 1
    else:
        # 증가하는 수열이라는 점이 무너지지 않고 LIS의 그리디한 성질을 계속 유지 할 수있다.
        ret[lower_bound(ret,array[x])] = array[x]
        x += 1
    print(ret)

print(count)