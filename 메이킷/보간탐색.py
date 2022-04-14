def interpolation(key, n):

    low = 0
    high = n - 1

    while (list[high] >= key and key > list[low]):
        j = int(((key-list[low]) / (list[high]-list[low])) * (high- low) +low)

        if key > list[j]:
            low = j + 1
        elif key < list[j]:
            high = j - 1
        else:
            low = j

    if list[low] == key: return low
    else: return -1

list = [3,9,15,22,31,55,67,88,89,91]
print(interpolation(15,len(list)))