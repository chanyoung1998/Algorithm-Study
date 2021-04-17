'''
내용:백준 알고리즘 단계별 풀기 투 포인터  1450 냅색 문제
날짜:21년4월 17일
사용 언어:파이썬
'''

import sys

subset = []

def make_subsetofA(i):
    if i == len(a):
        subsetsumsofA.append(sum(subset))
        return
    subset.append(a[i])
    make_subsetofA(i+1)
    subset.remove(a[i])
    make_subsetofA(i+1)
    return

def make_subsetofB(i):
    if i == len(b):
        subsetsumsofB.append(sum(subset))
        return
    subset.append(b[i])
    make_subsetofB(i+1)
    subset.remove(b[i])
    make_subsetofB(i+1)
    return

def upperbound(target,array):
    start = 0
    end = len(array)

    while start < end:
        mid = (start+end)//2

        if array[mid] > target:
            end = mid
        else:
            start = mid + 1

    return end

n,c = map(int,sys.stdin.readline().rstrip().split())
weights = list(map(int,sys.stdin.readline().rstrip().split()))

a = weights[:n//2]
b = weights[n//2:]
a.sort()
b.sort()
subsetsumsofA = []
make_subsetofA(0)
subsetsumsofA.sort()
subsetsumsofB = []
make_subsetofB(0)
subsetsumsofB.sort()

count = 0
for i in subsetsumsofA:
    target = c - i
    index = upperbound(target,subsetsumsofB) - 1
    if index >= 0:
        count += index+1

print(count)




