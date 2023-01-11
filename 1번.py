# x자리에서 y자리로  최대 z번 만큼 좌우 이동 가능할 때 최대 이동 가능 한 자리의 번호 , 불가능하면 -1

def solution(x,y,z):
    if x == y:
        return x + (z//2)
    elif x < y:
        if y -x > z:
            return -1
        else:
            left = z - (y-x)
            return y + left // 2
    else:
        if x - y > z:
            return -1
        else:
            left = z - (x-y)
            return x + left // 2
