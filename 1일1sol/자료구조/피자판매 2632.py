'''
24 03 03
피자판매
2632
골2
자료구조, 해쉬,


'''

import sys
from collections import defaultdict



totalSize = int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().strip().split(' '))
a = []
b = []
for _ in range(m):
    a.append(int(sys.stdin.readline()))

for _ in range(n):
    b.append(int(sys.stdin.readline()))

dictA = defaultdict(int)
dictB = defaultdict(int)

dictA[sum(a)] += 1
dictB[sum(b)] += 1

if len(a) > 1:
    for i in range(m):
        size = a[i]
        dictA[size] += 1
        j = (i + 1) % m
        while ((i - 1) % m) != j:
            size += a[j]
            if size <= totalSize:
                dictA[size] += 1
            else:
                break
            j = (j + 1) % m

if len(b) > 1:
    for i in range(n):
        size = b[i]
        dictB[size] += 1
        j = (i + 1) % n
        while ((i - 1) % n) != j:
            size += b[j]
            if size <= totalSize:
                dictB[size] += 1
            else:
                break
            j = (j + 1) % n

ret = 0
dictA[0] = 1 # keyB 가 totalSize인 경우 처리하기 위해
for sizeA, countA in dictA.items():
    keyB = totalSize - sizeA
    if keyB == 0:
        ret += countA
    elif keyB in dictB.keys():
        ret += countA * dictB[keyB]

print(ret)

'''
testcase
1
1 1
1
1
---
6
3 3
1
1
1
1
1
1
'''