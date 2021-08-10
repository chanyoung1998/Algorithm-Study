import sys
from itertools import permutations
n = int(sys.stdin.readline())
arrays = list(sys.stdin.readline().rstrip().split())
num = list(range(10))
ret = []
for permutation in permutations(num,n+1):

    flag = True
    for i in range(len(arrays)):
        if arrays[i] == '<':
           if permutation[i] >= permutation[i+1]:
               flag = False
               break
        elif arrays[i] == '>':
            if permutation[i] <= permutation[i+1]:
                flag = False
                break
    if flag:
        ret.append(permutation)


for i in ret[-1]:
    print(i,end='')
print()
for i in ret[0]:
    print(i,end='')
