import sys

R,C = map(int,sys.stdin.readline().strip().split(' '))
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
directions = list(map(int,list(sys.stdin.readline().strip())))
crazy = []
zongsu = []

dx = [1,1,1,0,0,0,-1,-1,-1]
dy = [-1,0,1,-1,0,1,-1,0,1]

for i in range(R):
    for j in range(C):
        if board[i][j] == 'R':
           crazy.append([i,j,False])
        elif board[i][j] == 'I':
            zongsu = [i,j]

for i,d in enumerate(directions):

    nx,ny = zongsu[0] + dx[d-1] , zongsu[1] + dy[d-1]
    zongsu = [nx,ny]
    newCrazy = []
    for c,(crazyX,crazyY,destroy) in enumerate(crazy):
        if not destroy:
            if crazyX == zongsu[0] and crazyY == zongsu[1]:
                print(f'kraj {i+1}')
                exit(0)

            minDistance = sys.maxsize
            minDir = 0
            for j in range(9):
                crazyNx,crazyNy = crazyX + dx[j], crazyY + dy[j]
                if 0 <= crazyNx < R and 0<= crazyNy < C:
                    distance = abs(crazyNx-zongsu[0]) + abs(crazyNy-zongsu[1])
                    if distance < minDistance:
                        minDistance = distance
                        minDir = j

            crazyNx, crazyNy = crazyX + dx[minDir], crazyY + dy[minDir]
            crazy[c][0] = crazyNx
            crazy[c][1] = crazyNy
            if crazyNx == zongsu[0] and crazyNy == zongsu[1]:
                print(f'kraj {i + 1}')
                exit(0)

    destroyIndex = set()
    for w in range(len(crazy)):
        for z in range(len(crazy)):
            if w == z:
                continue
            if (not crazy[w][2]) and  (not crazy[z][2]) and crazy[w][0] == crazy[z][0] and crazy[w][1] == crazy[z][1]:
                destroyIndex.add(w)
                destroyIndex.add(z)
    for di in range(len(crazy)):
        if di in destroyIndex:
            continue
        else:
            newCrazy.append(crazy[di])

    crazy = newCrazy

    # for di in destroyIndex:
    #     crazy[di][2] = True


ret = [['.' for _ in range(C)] for _ in range(R)]

for crazyX,crazyY,destroy in crazy:
    if not destroy:
        ret[crazyX][crazyY] = 'R'

ret[zongsu[0]][zongsu[1]] = 'I'

for re in ret:
    for r in re:
        print(r,end='')

    print()


