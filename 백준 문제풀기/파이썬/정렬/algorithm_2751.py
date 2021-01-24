''' 
내용:백준 알고리즘 정렬 2751번 수 정렬하기2-병합정렬
날짜:21년1월16일 
사용 언어:파이썬
'''


def mergesort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    i = 0
    j = 0
    list1 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list1.append(left[i]) 
            i += 1
        elif left[i] > right[j]:
            list1.append(right[j]) 
            j += 1
        
        
    while i < len(left):
        list1.append(left[i])
        i += 1
        
        
    while j < len(right):
        list1.append(right[j]) 
        j += 1
        
    
    return list1


def merge_sort(array):
    if len(array)<=1:
        return array
    
    # 재귀함수를 이용해서 끝까지 분할
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    # 분할된 배열끼리 비교
    while i<len(left) and j <len(right):
        if left[i]<right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    # 먼저 끝났을 때 
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1
    return array

a = [1,5,2,3,4,6,9,10]
print(mergesort(a))
