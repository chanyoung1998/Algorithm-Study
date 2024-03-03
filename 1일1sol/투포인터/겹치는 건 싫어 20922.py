import sys
from collections import defaultdict

n, k = map(int,sys.stdin.readline().strip().split(' '))
arrays = list(map(int,sys.stdin.readline().strip().split(' ')))
check = defaultdict(int)
start = 0
end = 0
ret = 0
while end < n:

    num = arrays[end]

    if check[num] + 1 > k:
        while start <= end and check[num] + 1 > k:
            numToOut = arrays[start]
            check[numToOut] -= 1
            start += 1

    check[num] += 1
    ret = max(ret,end-start + 1)
    
    end += 1


print(ret)



