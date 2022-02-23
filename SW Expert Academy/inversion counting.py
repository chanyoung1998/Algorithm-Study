sorted = [0 for _ in range(100001)]

def merge(left,mid,right):
    global ret

    if left >= right:
        return 0

    lp = left
    rp = mid+1
    idx = left

    while lp <= mid and rp <= right:
        if array[lp] <= array[rp]:
            sorted[idx] = array[lp]
            idx += 1
            lp += 1
        else:
            ret += mid-lp + 1
            sorted[idx] = array[rp]
            idx+=1
            rp += 1

    if lp > mid:
        while rp <= right:
            sorted[idx] = array[rp]
            idx += 1
            rp += 1
    else:
        while lp <= mid:

            sorted[idx] = array[lp]
            idx += 1
            lp += 1

    for i in range(left,right+1):
        array[i] = sorted[i]






def divide(left,right):

    if left >= right:
        return
    mid = (left+right)// 2
    divide(left,mid)
    divide(mid+1,right)
    merge(left,mid,right)


T = int(input())
for t in range(1,T+1):

    n = int(input())
    array = list(map(int,input().rstrip().split()))
    ret = 0

    divide(0,n-1)
    print('#{} {}'.format(t,ret))

