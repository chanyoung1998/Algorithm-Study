import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
maps = [list(map(int, sys.stdin.readline().strip().split(' '))) for _  in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

ret = 0
def backtracking(x, y, total):
    global ret

    case1 = [(x, y), (x, y - 1), (x + 1, y)]

    # case 2
    case2 = [(x, y), (x, y - 1), (x - 1, y)]

    # case 3
    case3 = [(x, y), (x, y + 1), (x - 1, y)]

    # case 4
    case4 = [(x, y), (x, y + 1), (x + 1, y)]

    cases = [case1,case2,case3,case4]

    for case in cases:
        flag = True
        for cx, cy in case:
            if not ((0 <= cx < N) and (0 <= cy < M) and (not visit[cx][cy])):
                flag = False
                break

        if flag:
            for cx, cy in case:
                visit[cx][cy] = True
                total += maps[cx][cy]
            total += maps[x][y]

            if y != M - 1:
                backtracking(x, y + 1, total)
            else:
                if x != N - 1:
                    backtracking(x + 1, 0, total)

            if x == N - 1 and y == M - 1:
                ret = max(ret, total)

            for cx, cy in case:
                visit[cx][cy] = False
                total -= maps[cx][cy]
            total -= maps[x][y]

    # case 5
    if y != M - 1:
        backtracking(x, y + 1, total)
    else:
        if x != N - 1:
            backtracking(x + 1, 0, total)


    if x == N-1 and y == M-1:
        ret = max(ret, total)

    return

backtracking(0,0,0)
print(ret)