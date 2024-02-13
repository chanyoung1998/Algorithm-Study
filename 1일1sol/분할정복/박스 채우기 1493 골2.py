'''
2024 02 12
박스 채우기
골2
분할정복
'''
import sys
sys.setrecursionlimit(2000000)

L, W, H = map(int, sys.stdin.readline().strip().split(' '))
N = int(sys.stdin.readline())
CUBE = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]
ret = 0

# a b c
# (l-a,b,c), (a, w-b,c) , (l-a,w-b,c) (l,w,h-c)
def solve(l, w, h):
    global ret

    if l == 0 or w == 0 or h == 0:
        return True

    for i in range(len(CUBE) - 1, -1, -1):
        cur = 1 << CUBE[i][0]
        count = CUBE[i][1]
        if count > 0 and l >= cur and w >= cur and h >= cur:
            ret += 1
            CUBE[i][1] -= 1
            a = solve(l - cur, cur, cur)
            b = solve(cur, w - cur, cur)
            c = solve(l - cur, w - cur, cur)
            d = solve(l, w, h - cur)

            return a and b and c and d

    return False


if solve(L, W, H):
    print(ret)
else:
    print(-1)
