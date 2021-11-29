import sys

n = int(sys.stdin.readline())
inputs = list(map(int,sys.stdin.readline().rstrip().split()))

def merge(array,left,mid,right):

    lp = left
    rp = mid+1
    sorted_array = []
    while lp <= mid and rp <= right:
        if array[lp] < array[rp]:
            sorted_array.append(array[lp])
            lp += 1
        else:
            sorted_array.append(array[rp])
            rp += 1

    if lp > mid:
        for i in range(rp,right+1):
            sorted_array.append(array[i])

    elif rp > right:
        for i in range(lp,mid+1):
            sorted_array.append(array[i])

    for i in range(left,right+1):
        inputs[i] = sorted_array[i-left]



def merge_sort(array,left,right):

    if left < right:
        mid = (left+right)//2
        merge_sort(array,left,mid)
        merge_sort(array,mid+1,right)
        merge(array,left,mid,right)

merge_sort(inputs,0,n-1)
print(inputs)
