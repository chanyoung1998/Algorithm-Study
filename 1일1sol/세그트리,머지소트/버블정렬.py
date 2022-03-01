import sys

n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().rstrip().split()))
temp = [0 for _ in range(n)]
def divide(start,end):

    if start >= end:
        return 0

    mid = (start+end)//2

    l = divide(start,mid)
    r = divide(mid+1,end)

    m = merge(start,mid,end)

    return l+m+r

def merge(start,mid,end):

    lp = start
    rp = mid+1
    idx = start

    cnt = 0
    while lp <= mid and rp <= end:
        if array[lp] <= array[rp]: # 등호가 여기에 들어가야한다!
            temp[idx] = array[lp]

            #왼쪽은 정렬된 상태 ->cnt해줄 필요 x
            # cnt += lp-idx
            idx +=1
            lp += 1

        else:
            temp[idx] = array[rp]

            cnt += rp-idx
            idx += 1
            rp += 1

    if rp > end:
        while lp <= mid:
            temp[idx] = array[lp]
            idx += 1
            lp += 1
    else:
        while rp <= end:
            temp[idx] = array[rp]
            idx += 1
            rp += 1


    for i in range(start,end+1):
        array[i] = temp[i]

    return cnt


print(divide(0,n-1))