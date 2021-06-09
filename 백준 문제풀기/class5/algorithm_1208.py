import sys
from itertools import combinations
n, s = map(int,sys.stdin.readline().rstrip().split())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
numbers_1 = numbers[:n//2]
numbers_2 = numbers[n//2:]


def subsetsum(numbers):
    subsetsum = []
    for i in range(len(numbers)+1):
        for subsets in combinations(numbers,i):
            subsetsum.append(sum(subsets))
    return subsetsum

subsetsum_numbers1 = subsetsum(numbers_1)
subsetsum_numbers2 = subsetsum(numbers_2)
subsetsum_numbers2.sort()

def first(array,target,start,end):
    if start > end:
        return None

    mid = (start+end)//2

    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array,target,start,mid-1)
    else:
        return first(array,target,mid+1,end)


def last(array, target, start, end):

    '''mid = (start + end) // 2

    if (mid == n-1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)'''
    while start <= end:
        mid = (start+end)//2

        if (mid == len(array)-1 or target < array[mid+1]) and target == array[mid]:
            return mid

        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1

    return None

count = 0
for x in subsetsum_numbers1:
    start = 0
    end = len(subsetsum_numbers2)-1
    target = s - x

    l = first(subsetsum_numbers2,target,0,len(subsetsum_numbers2)-1)
    r = last(subsetsum_numbers2,target,0,len(subsetsum_numbers2)-1)

    if l == None:
        continue

    count += r-l+1

if s == 0:
    print(count-1)
else:
    print(count)
