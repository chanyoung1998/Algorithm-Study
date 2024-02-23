'''
24 02 23
구간 곱 구하기 11505
골1
세그먼트트리
'''

import sys, math


N, M, K = map(int, input().strip().split(' '))
numbers = []
H = math.ceil(math.log2(N)) + 1
segTree = [1 for _ in range(1 << H)]
MOD = 1000000007


def makeSegTree(idx, start, end):
    if start == end:
        segTree[idx] = numbers[start] % MOD
        return segTree[idx]

    mid = (start + end) // 2
    left = makeSegTree(2 * idx, start, mid)
    right = makeSegTree(2 * idx + 1, mid + 1, end)

    segTree[idx] = (left * right) % MOD
    return segTree[idx]


def updateSegTree(idx, start, end, targetIdx, targetValue):

    if targetIdx < start or end < targetIdx:
        return segTree[idx]

    if( start == end )and (start == targetIdx):
        segTree[idx] = targetValue % MOD
        return segTree[idx]
    elif start == end:
        return segTree[idx]

    mid = (start + end) // 2
    left = updateSegTree(2 * idx, start, mid, targetIdx, targetValue)
    right = updateSegTree(2 * idx + 1, mid + 1, end, targetIdx, targetValue)

    segTree[idx] = (left * right) % MOD
    return segTree[idx]


def find(idx, start, end, x, y):
    if y < start or x > end:
        return 1

    if x <= start and end <= y:
        return segTree[idx]

    mid = (start + end) // 2
    left = find(2 * idx, start, mid, x, y)
    right = find(2 * idx + 1, mid + 1, end, x, y)

    return (left * right) % MOD


for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

makeSegTree(1, 0, N - 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().strip().split(' '))
    if a == 1:
        updateSegTree(1, 0, N - 1, b - 1, c)
    else:
        print(find(1, 0, N - 1, b - 1, c - 1))
