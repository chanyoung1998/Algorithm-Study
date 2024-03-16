import sys

A,B  = map(int,sys.stdin.readline().strip().split(' '))
N,M = map(int,sys.stdin.readline().strip().split(' '))

robots = []
direction = [0,1,2,3]
dx = [0,-1,0,1] # 동 남 서 북
dy = [1,0,-1,0]


for _ in range(N):
    y,x,dir = sys.stdin.readline().strip().split(' ')
    if dir == 'E':
        dir = 0
    elif dir =='S':
        dir = 1
    elif dir =='W':
        dir = 2
    else:
        dir = 3

    robots.append([int(x),int(y),dir])

for _ in range(M):
    robot,cmd,repeat = sys.stdin.readline().strip().split(' ')
    robot = int(robot)
    repeat = int(repeat)
    curX, curY, curDir = robots[robot - 1]

    if cmd == 'L':
        nextDir = (curDir - repeat) % 4
        robots[robot - 1] = [curX, curY, nextDir]
    elif cmd == 'R':
        nextDir = (curDir + repeat) % 4
        robots[robot - 1] = [curX, curY, nextDir]
    elif cmd =='F':

        for r in range(repeat):
            nextX,nextY = curX + dx[curDir], curY + dy[curDir]

            if 1 <= nextX <= B and 1<= nextY <= A:
                pass
            else:
                print(f'Robot {robot} crashes into the wall')
                exit(0)

            for i in range(N):
                if i != robot-1:
                    if robots[i][0] == nextX and robots[i][1] == nextY:
                        print(f'Robot {robot} crashes into robot {i+1}')
                        exit(0)

            curX,curY = nextX,nextY

        robots[robot-1] = [curX,curY,curDir]

print('OK')