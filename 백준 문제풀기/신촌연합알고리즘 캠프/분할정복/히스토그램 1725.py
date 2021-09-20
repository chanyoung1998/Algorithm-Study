import sys


n = int(sys.stdin.readline())
height = []

for _ in range(n):
    height.append(int(sys.stdin.readline()))
#print(height)

def merge(l,r,mid):
    nl = mid
    nr = mid+1
    nh = min(height[nl],height[nr])
    area = nh * 2
    cnt = 2
    while True:
        if (height[nl] == 0 or nl == l) and (height[nr] == 0 or nr == r):
            break
        elif height[nl] == 0 or nl == l:
            if height[nr + 1] < nh:
                nh = height[nr + 1]
            nr += 1
        elif height[nr] == 0 or nr == r:
            if height[nl - 1] < nh:
                nh = height[nl - 1]
            nl -= 1
        else:
            if height[nl - 1] > height[nr + 1]:
                if height[nl - 1] < nh:
                    nh = height[nl - 1]
                nl -= 1
            else:
                if height[nr + 1] < nh:
                    nh = height[nr + 1]
                nr += 1
        cnt += 1
        area = max(area, nh * cnt)

    return area


def divide(l,r):

    if l == r:
        return height[l]
    if l < r:
        mid = (l+r) // 2
        left = divide(l,mid)
        right = divide(mid+1,r)
        return max(left,right,merge(l,r,mid))

print(divide(0,n-1))