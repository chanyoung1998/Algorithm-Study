import sys

n = int(sys.stdin.readline())
occupied = list(map(int,sys.stdin.readline().rstrip()))
cnt = 0
space = []
side = []

check = False
for i in range(len(occupied)):
    if occupied[i] == 0:
        cnt +=1
    elif occupied[i] == 1:
        if not check:
            if cnt > 0:
                side.append(cnt)
            check = True
        else:
            if cnt > 0:
                space.append(cnt)
        cnt = 0

if cnt > 0:
    side.append(cnt)

#모두 0인 경우
if not check:
    print(n-1)
    exit(0)

space.sort(reverse=True)
ret = []
if len(side) == 0: #양 끝에 빈 공간 존재x
    if len(space) > 1:
        ret.append(min((space[0]+1) // 2,(space[1]+1)//2)) # 두 공간에 각 각의 소 넣기

    ret.append((space[0]+2)//3) # 한 공간에 2마리 소 넣기
elif len(side) == 1:

    #두 공간에 두 마리 배치하는 경우
    if len(space) > 1: # 둘다 space에
        ret.append((space[1]+1)//2)

    if len(space) > 0:
        if side[0] > (space[0]+1)//2: # 한 마리는 side에 넣는 경우
            ret.append((space[0]+1)//2)
        else:
            ret.append(side[0])


    #한 공간에 두 마리 배치하는 경우
    ret.append(side[0]//2) # 사이드에 두마리
    if len(space) > 0:
        ret.append((space[0]+2)//3) # space에 두마리


else:

    if len(space) == 0:
        ret.append(min(side))
    elif len(space) == 1:
        s1 = side[0]
        s2 = side[1]
        s3 = (space[0]+1)//2
        min_s = min(s1,s2,s3)
        temp = set({s1,s2,s3}) - {min_s}
        temp = list(temp)
        ret.append(min(temp[0],temp[1]))
    else:
        temp = [side[0],side[1]]
        if len(space) > 1:
            temp.append((space[0]+1)//2)
            temp.append((space[1]+1)//2)
        elif len(space) == 1:
            temp.append((space[0]+1)//2)
        temp.sort(reverse=True)
        ret.append(temp[1])




    if len(space) > 0:
        ret.append((space[0] + 2) // 3)

    ret.append(max(side[0] // 2,side[1]//2))

ret.sort(reverse=True)
# print(ret)
# print(space)
# print(side)

if len(space) > 0:
    print(min(space)+1 if min(space)+1 < ret[0] else ret[0])
else:
    print(ret[0])




