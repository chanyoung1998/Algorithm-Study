import sys

def sol(string):


    global flag
    if len(string) == 0:
        flag = True
        return True

    if len(string) == 1:
        return False



    i = 0
    while i < len(string)-1:
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                if j == len(string)-1:
                    if sol(string[:i]):
                        return True
                    i = j+1
                continue
            else:
                if j == i + 1:
                    i += 1
                    break
                else:
                    if sol(string[:i] + string[j:]):
                        return True
                    i = j

    return False


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    s = list(sys.stdin.readline().rstrip())
    flag = False
    check = {}
    sol(s)
    if flag:
        print(1)
    else:
        print(0)


'''
import re

def solve(s):
    group = [(m.start(0), m.end(0)) for m in re.finditer('aa+|bb+', s)]
    if len(group) == 0: return 0
    if len(set(s)) == 1: return 1
    for g in group:
        if solve(s[0:g[0]] + s[g[1]:]) == 1: return 1
    return 0

strings = [input() for _ in range(int(input()))]
for string in strings:
    print(solve(string))
    


'''