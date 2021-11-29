import sys

def lowerbound(array,start,end,target):

    while start + 1 < end:
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid
        else:
            start = mid

    return end

def upperbound(array,start,end,target):

    while start + 1 < end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        else:
            start = mid

    return end
array = [1,1,2,3,3,3,4,4,6,7,7,8,8,9,10]

print(lowerbound(array,0,len(array),3))

print(upperbound(array,0,len(array),3))


