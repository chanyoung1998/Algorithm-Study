import sys
import math
n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
count = 0


def merge(left,right):
    global count
    temp = []
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            count += right_pointer
            temp.append(left[left_pointer])
            left_pointer += 1

        elif left[left_pointer] > right[right_pointer]:
            temp.append(right[right_pointer])
            right_pointer += 1

    if left_pointer == len(left):
        temp += right[right_pointer:]
    else:
        count += len(left[left_pointer:]) * len(right)
        temp += left[left_pointer:]

    return temp

def divide(array,l,r):
    if l==r:
        return [array[l]]
    if l < r:
        mid = (l+r) // 2
        left = divide(array,l,mid)
        right = divide(array,mid+1,r)
        return merge(left,right)

divide(numbers,0,n-1)
print(count)




