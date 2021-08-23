import sys
import copy
from itertools import permutations
n,m,k = map(int,sys.stdin.readline().rstrip().split())
org_array = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
rotates = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(k)]




def rotate(operation,array):

    temp_array = copy.deepcopy(array)
    result = sys.maxsize
    for i in range(k):
        r = operation[i][0] - 1
        c = operation[i][1] - 1
        s = operation[i][2]
        x, y = r-s, c-s
        p, q = r+s, c+s

        while x < p and y < q:
            temp1 = temp_array[x][q]
            for i in range(q,y,-1):
                temp_array[x][i] = temp_array[x][i-1]


            temp2 = temp_array[p][q]
            for i in range(p,x+1,-1):
                temp_array[i][q] = temp_array[i-1][q]
            temp_array[x+1][q] = temp1

            temp3 = temp_array[p][y]
            for i in range(y,q-1):
                temp_array[p][i] = temp_array[p][i+1]
            temp_array[p][q-1] = temp2

            for i in range(x,p-1):
                temp_array[i][y] =temp_array[i+1][y]
            temp_array[p-1][y] = temp3
            x += 1
            y += 1
            p -= 1
            q -= 1

    for arr in temp_array:
        result = min(result,sum(arr))

    return result


ret = sys.maxsize
for rot in permutations(rotates):
    val = rotate(list(rot),org_array)
    ret = min(ret,val)
print(ret)