'''
24 02 26
K진 트리
11812번
골3
트리, 최소 공통 조상
'''

import sys, math


# 완전 k진 트리-> 끝 번호 1, 1 + k^1, 1 + k^1 + k^2
# x번 째라면 -> 부모는 몇 번째?
# 1. x 깊이 구하기 h
# 2. x가 몇 번째 그룹에 속하는지 구하기 n번째 그룹이라면 -> 부모는 h-1 번째 높이에서 n번째


def getHeight(x,k):
    i,cnt = 0,0
    while 1:
        cnt += k**i
        if cnt >= x:
            return i
        i += 1


def getGroup(x, k, h):
    start = getStart(k, h)
    return int((x - start) // k)


def getStart(k, h):
    if h == 0:
        return 1

    return int((k ** h - 1) / (k - 1)) + 1


def getParent(x, k):
    if x == 1:
        return 1

    h = getHeight(x, k)
    g = getGroup(x, k, h)
    p = getStart(k, h - 1) + g
    return int(p)


def getLCA(x, y, k):
    mv = 0
    xh = getHeight(x, k)
    yh = getHeight(y, k)

    if xh < yh:
        x, y = y, x
        xh, yh = yh, xh

    while xh != yh:
        x = getParent(x, k)
        xh -= 1
        mv += 1

    while x != y:
        x = getParent(x, k)
        y = getParent(y, k)
        mv += 2

    return mv


n, k, q = map(int, sys.stdin.readline().strip().split(' '))
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split(' '))
    if k == 1:
        print(abs(x-y))
        continue
    print(getLCA(x, y, k))
