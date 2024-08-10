'''
24 06 16
A와 B 2
12919
골5

'''
import sys

def addA(str):
    return str + "A"

def addBandReverse(str):
    return (str + "B")[::-1]

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
visit = set()
lengthT = len(T)

def dfs(cur,length):

    if length == lengthT:
        if cur == T:
            return 1
        else:
            return 0

    opA = addA(cur)
    opB = addBandReverse(cur)
    retA = 0
    retB = 0
    if(opA not in visit):
        visit.add(opA)
        retA = dfs(opA,length+1)

    if(opB not in visit):
        visit.add(opB)
    retB = dfs(opB,length+1)


    return retA | retB

def dfs2(cur):


    if len(cur) == 0:
        return 0
    if cur == S:
        return 1

    ret = 0
    ret2 = 0
    if cur[-1] == 'A':
        ret = dfs2(cur[:-1])

    if cur[0] == 'B':
        ret2 = dfs2(cur[1:][::-1])

    return ret | ret2

print(dfs2(T))
