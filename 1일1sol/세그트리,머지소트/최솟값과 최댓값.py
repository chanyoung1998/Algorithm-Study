'''
24 02 22
최솟값과 최댓값
백준 2357
골1
세그트리
'''
import sys, math
sys.setrecursionlimit(10 ** 8) # 재귀 깊이 제한 늘리기

def makeSegTree(idx, start, end):
    if start == end:
        segTree[idx] = (number[start], number[start])
        return segTree[idx]

    mid = (start + end) // 2
    left = makeSegTree(idx * 2, start, mid)
    right = makeSegTree(idx * 2 + 1, mid + 1, end)

    segTree[idx] = (min(left[0], right[0]), max(left[1], right[1]))

    return segTree[idx]


def find(idx, start, end, x, y):
    if y < start or x > end:
        return (sys.maxsize, -sys.maxsize)

    if x <= start and end <= y:
        return segTree[idx]

    mid = (start + end) // 2
    left = find(2 * idx, start, mid, x, y)
    right = find(2 * idx + 1, mid + 1, end, x, y)
    return min(left[0], right[0]), max(left[1], right[1])


N, M = map(int, sys.stdin.readline().strip().split(" "))
number = []
H = math.ceil(math.log2(N)) + 1
segTree = [(sys.maxsize, -sys.maxsize) for _ in range(2 ** H)]

for _ in range(N):
    number.append(int(sys.stdin.readline()))

makeSegTree(1, 0, N - 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    print(*find(1, 0, N - 1, a - 1, b - 1))
