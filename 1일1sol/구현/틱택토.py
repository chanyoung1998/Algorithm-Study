'''
24 02 27
틱택토
7682
골5

'''

import sys

def check_game_end(case, typ):
    if case[0] == typ and case[0] == case[1] == case[2]:
        return True
    elif case[0] == typ and case[0] == case[3] == case[6]:
        return True
    elif case[4] == typ and case[1] == case[4] == case[7]:
        return True
    elif case[4] == typ and case[3] == case[4] == case[5]:
        return True
    elif case[8] == typ and case[6] == case[7] == case[8]:
        return True
    elif case[8] == typ and case[2] == case[5] == case[8]:
        return True
    elif case[4] == typ and case[0] == case[4] == case[8]:
        return True
    elif case[4] == typ and case[2] == case[4] == case[6]:
        return True
    else:
        return False


def solve(tictacto, count):
    if check_game_end(tictacto, 'O') or check_game_end(tictacto, 'X') or count == 9:
        tictactoSet.add(tuple(tictacto))
        return

    if count != 9:

        if count % 2 == 0:
            type = 'X'
        else:
            type = 'O'

        for i in range(9):
            if tictacto[i] == '.':
                tictacto[i] = type
                solve(tictacto, count + 1)
                tictacto[i] = '.'


tictactoSet = set()
solve(['.', '.', '.', '.', '.', '.', '.', '.', '.'],0)

while True:
    case = sys.stdin.readline().strip()
    if case == 'end':
        break

    case = tuple(case)
    if case in tictactoSet:
        print('valid')
    else:
        print('invalid')
