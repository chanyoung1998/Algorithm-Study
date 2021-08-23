import sys
import copy

n,m,k = map(int,sys.stdin.readline().rstrip().split())
array = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
rotates = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(k)]
rotates = [list(map(lambda x: x-1,rotates[i])) for i in range(k)]



def rotate(r,c,s):
    if s < 0:
        return

    x, y = r-s, c-s
    p, q = r+s, c+s

    temp1 = array[x][q]
    for i in range(q,y,-1):
        array[x][i] = array[x][i-1]


    temp2 = array[p][q]
    for i in range(p,x+1,-1):
        array[i][q] = array[i-1][q]
    array[x+1][q] = temp1

    temp3 = array[p][y]
    for i in range(y,q-1):
        array[p][i] = array[p][i+1]
    array[p][q-1] = temp2

    for i in range(x,p-1):
        array[i][y] =array[i+1][y]
    array[p-1][y] = temp3

    for a in array:
        print(a)

    return



for a in array:
    print(a)
print('')
rotate(2,3,1)
