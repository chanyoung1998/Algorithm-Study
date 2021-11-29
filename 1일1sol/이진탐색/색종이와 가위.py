import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

lo = -1
hi = n //2 + 1

while lo + 1 < hi:

    mid = (lo + hi) // 2

    if (mid + 1) * (n - mid + 1) >= k:
        hi = mid
    else:
        lo = mid

if (hi + 1) * (n - hi + 1) == k:
    print('YES')
else:
    print('NO')
