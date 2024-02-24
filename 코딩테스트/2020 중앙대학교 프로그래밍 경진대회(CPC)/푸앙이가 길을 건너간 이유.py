import sys
a,b,c = map(int,sys.stdin.readline().rstrip().split())
x1,x2,y1,y2 = map(int,sys.stdin.readline().rstrip().split())

if a != 0 and b != 0:
    fx1 = round(-(a/b) * x1 - (c/b),10)
    fx2 = round(-(a/b) * x2 - (c/b),10)

    if fx1 >= y2 and fx2 >= y2:
        print("Lucky")
    elif fx1 >= y2 > fx2:
        print("Poor")
    elif y2 > fx1 > y1:
        print("Poor")
    elif fx1 <= y1 and fx2 <= y1:
        print("Lucky")
    elif fx1 <= y1 < fx2:
        print("Poor")

elif a != 0 and b == 0:
    x = -(c/a)

    if x >= x2 or x <= x1:
        print("Lucky")
    else:
        print("Poor")

elif b != 0 and a == 0:
    y = -(c/b)

    if y >= y2 or y <= y1:
        print("Lucky")
    else:
        print("Poor")
