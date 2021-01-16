def Merge_sort(arr):


    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low_arr = Merge_sort(arr[:mid])
    high_arr = Merge_sort(arr[mid:])

    #데이터 집합을 반으로 나누는 과정(Divide)

    merged_arr= [] # return하기 위한 전체 배열
    l = h = 0

    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l +=1
        else:
            merged_arr.append(high_arr[h])
            h +=1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    #데이터를 다시 합치는 것 (Combine)

    return merged_arr

list = [1,5,7,2,3,6,10,9]
result = Merge_sort(list)
print(result)