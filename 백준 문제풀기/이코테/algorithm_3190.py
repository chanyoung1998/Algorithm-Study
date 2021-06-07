'''
내용:백준 알고리즘 1439 이코테 뱀
날짜:21년5월31일
사용 언어:파이썬
'''

import sys
import copy
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = []
for _ in range(k):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    apple.append((x-1,y-1))

l = int(sys.stdin.readline())
move = []
for _ in range(l):
    x, l = sys.stdin.readline().rstrip().split()
    move.append([int(x),l])


snake = [[0,0]]
direct = [[0,1],[1,0],[0,-1],[-1,0]]#우,하,좌,상
cur_direct = 0
head = [0,0]
tail = [0,0]
time = 0

dct = 0
direction_change_time = move[dct][0]

while True:
    time += 1
    head[0] = head[0] + direct[cur_direct][0]
    head[1] = head[1] + direct[cur_direct][1]

    # head가 경계선 밖으로 나갈 때 or 자기 몸이랑 만날 때
    # break
    if (head[0] < 0 or head[0] >= n) or (head[1] < 0 or head[1] >= n ):
        break
    elif len(snake) >= 2 and head in snake[1:]:
        break

    if (head[0],head[1]) in apple:
        apple.remove((head[0],head[1]))

        if len(snake) == 1:
            snake[0] = copy.deepcopy(head)
            temp = copy.deepcopy(tail)
            snake.append(temp)
        else:
            for i in range(len(snake)-1,0,-1):
                snake[i] = copy.deepcopy(snake[i-1])
            snake[0] = copy.deepcopy(head)
            temp = copy.deepcopy(tail)
            snake.append(temp)
    else: # 사과를 못 먹었을 때
        if len(snake) == 1:
            snake[0] = copy.deepcopy(head)
            tail = copy.deepcopy(snake[-1])
        else:
            for i in range(len(snake)-1,0,-1):
                snake[i] = copy.deepcopy(snake[i - 1])
            snake[0] = copy.deepcopy(head)
            tail = copy.deepcopy(snake[-1])

    if direction_change_time == time:
        if move[dct][1] == 'D': #오른쪽으로 90도 회전
            cur_direct = (cur_direct + 1) % 4
        elif move[dct][1] == 'L':
            cur_direct = (cur_direct - 1) % 4

        dct += 1
        if dct != len(move):
            direction_change_time = move[dct][0]


print(time)


































































































































