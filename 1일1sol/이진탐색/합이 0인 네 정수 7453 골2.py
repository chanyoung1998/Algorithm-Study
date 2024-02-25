'''
24 02 25
합이 0인 네 정수
7453
골2
이분탐색, 투포인터, map 등
'''

import sys
def lower(target):

    low = -1
    high = len(CD) -1

    while low + 1 < high:
        mid = (low+high) // 2

        if CD[mid] >= target:
            high = mid
        else:
            low = mid

    return high


def upper(target):
    low = -1
    high = len(CD) -1

    while low + 1 < high:
        mid = (low + high) // 2

        if CD[mid] > target:
            high = mid
        else:
            low = mid

    return high



n = int(sys.stdin.readline())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split(' '))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

CD = []

for i in range(n):
    for j in range(n):
        CD.append(C[i] + D[j])

CD.sort()
answer = 0
for i in range(n):
    for j in range(n):
        target = (A[i] + B[j]) * -1
        l = lower(target)
        u = upper(target)
        answer +=  (u-l)

print(answer)


