import sys

N,M,K = map(int,sys.stdin.readline().strip().split(' '))
stickers = []
visist = [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r,c = map(int,sys.stdin.readline().strip().split(' '))
    sticker = [list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(r)]
    stickers.append(sticker)


def rotateClockWise(sticker):
    row = len(sticker)
    col = len(sticker[0])
    newSticker = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            newSticker[j][row-i-1] = sticker[i][j]

    return newSticker

def check(x,y,sticker):
    
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            cx = x + i
            cy = y + j
            if 0 <= cx < N and 0 <= cy < M:
                if sticker[i][j] == 1 and visist[cx][cy]:
                    return False
            else:
                return False

    # 붙이기
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            cx = x + i
            cy = y + j
            if sticker[i][j] == 1:
                visist[cx][cy] = True
    
    return True




for sticker in stickers:
    rotateSticker = sticker

    for r in range(4):
        flag = False
        for i in range(N):
            for j in range(M):
                if check(i,j,rotateSticker):
                    flag = True
                    break
            if flag:
                break

        if flag:
            break
        else:
            rotateSticker = rotateClockWise(rotateSticker)


ret = 0
for v in visist:
    ret += sum(v)
print(ret)