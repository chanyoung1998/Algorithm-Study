'''
24 07 28
퍼즐 채우기
프로그래머스
level3

'''

from collections import deque, defaultdict

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
# direction = [0, 1, 2, 3]  # 위, 아래, 왼, 오
# turnMapping = {3: 1, 2: 0, 1: 2, 0: 3}
# goBackMapping = {0: 1, 1: 0, 2: 3, 3: 2}
maxCnt = 0

# 오 -> 아래
# 왼 -> 위
# 아래 -> 왼
# 위 -> 오

puzzlesTurned = []


def solution(game_board, table):
    global maxCnt, puzzlesTurned
    answer = 0
    puzzles = decompose(table, 1)
    spaces = decompose(game_board, 0)

    puzzleDict = defaultdict(list)
    spaceDict = defaultdict(list)

    for puzzle in puzzles:
        puzzleDict[len(puzzle)].append(puzzle)

    for space in spaces:
        spaceDict[len(space)].append(space)

    for size in puzzleDict.keys():
        puzzles = puzzleDict[size]
        spaces = spaceDict[size]
        for puzzle in puzzles:
            temp = []
            for i in range(4):
                puzzle = turnPuzzle2(puzzle)
                puzzle.sort()
                temp.append(puzzle)
            puzzlesTurned.append(temp)

        visitSpace = [False for _ in range(len(spaces))]
        visitpuzzle = [False for _ in range(len(puzzles))]

        for i in range(len(puzzles)):
            for j in range(len(spaces)):
                if not visitSpace[j] and not visitpuzzle[i] and checkIsFit(spaces[j],i):
                    visitpuzzle[i] = True
                    visitSpace[j] = True
                    answer += size


        answer += maxCnt
        maxCnt = 0
        puzzlesTurned = []
    return answer


def dfs(idx, puzzles, spaces, visitSpace, visitpuzzle, cnt):
    global maxCnt
    # if idx == len(puzzles) or sum(visitSpace) == len(spaces):
    #     maxCnt = max(maxCnt, cnt)
    #     return
    #
    # for i in range(len(spaces)):
    #     if not visitSpace[i] and not visitpuzzle[idx]:
    #         if checkIsFit(spaces[i], idx):
    #             cnt += len(puzzles[idx])
    #             visitSpace[i] = True
    #             visitpuzzle[idx] = True
    #             return dfs(idx + 1, puzzles, spaces, visitSpace, visitpuzzle, cnt)
    #         else:
    #             dfs(idx + 1, puzzles, spaces, visitSpace, visitpuzzle, cnt)
    #


def decompose(table, target):
    puzzles = []
    visit = set()
    for h in range(len(table)):
        for w in range(len(table[h])):
            if table[h][w] == target and (h, w) not in visit:
                dq = deque()
                puzzle = [(h, w)]
                visit.add((h, w))
                dq.append((h, w))
                while dq:
                    curH, curW = dq.popleft()
                    for i in range(4):
                        nextH, nextW = curH + dh[i], curW + dw[i]
                        if 0 <= nextH < len(table) and 0 <= nextW < len(table[h]) and (nextH, nextW) not in visit and \
                                table[nextH][nextW] == target:
                            puzzle.append((nextH, nextW))
                            visit.add((nextH, nextW))
                            dq.append((nextH, nextW))

                puzzles.append(sorted(puzzle))
    return puzzles


def turnPuzzle2(puzzle):
    return list(map(lambda x: (x[1], -x[0]), puzzle))


def checkIsFit(gameBoardDirectioon, puzzleIdx):
    puzzleTurn = puzzlesTurned[puzzleIdx]

    if len(gameBoardDirectioon) != len(puzzleTurn[0]):
        return False

    for _ in range(4):
        check = True
        puzzle = puzzleTurn[_]
        for i in range(len(puzzle)):
            dx, dy = puzzle[0][0] - gameBoardDirectioon[0][0], puzzle[0][1] - gameBoardDirectioon[0][1]
            puzzle = list(map(lambda x: (x[0] - dx, x[1] - dy), puzzle))
            if gameBoardDirectioon[i][0] != puzzle[i][0] or gameBoardDirectioon[i][1] != puzzle[i][1]:
                check = False
                break
        if check:
            return check

    return False


assert solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 0, 0]],
                [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                 [0, 1, 0, 0, 0, 0]]) == 14
