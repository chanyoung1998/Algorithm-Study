import sys

n = int(sys.stdin.readline())
inputs = list(map(int,sys.stdin.readline().rstrip().split()))

def QuickSort(array,left,right):

    if left >= right:
        return

    pivot = left
    lp = left+1
    rp = right

    while lp <= rp:

        while lp <= right and array[lp] <= array[pivot]:
            lp += 1
        while rp > left and array[rp] >= array[pivot]:
            rp -= 1

        if lp <= rp:
            array[lp],array[rp] = array[rp],array[lp]
        else:
            array[rp],array[pivot] = array[pivot],array[rp]

    QuickSort(array,left,rp-1)
    QuickSort(array,rp+1,right)

    return array

print(QuickSort(inputs,0,n-1))
