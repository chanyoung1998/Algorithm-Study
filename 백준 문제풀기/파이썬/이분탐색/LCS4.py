import sys
import bisect
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().rstrip().split()))
b = list(map(int,sys.stdin.readline().rstrip().split()))
b_transformed = [0 for _ in range(n)]
for i in range(n):
    index = b.index(a[i])
    b_transformed[index] = i

temp = []
temp.append(b_transformed[0])
for element in b_transformed[1:]:
    if temp[-1] < element:
        temp.append(element)
    else:
        temp[bisect.bisect_left(temp,element)] = element

    #print(temp)
print(len(temp))