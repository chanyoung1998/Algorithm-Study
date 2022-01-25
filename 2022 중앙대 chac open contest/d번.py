import sys

time = list(map(int,sys.stdin.readline().rstrip().split(':')))
time2 = time[0] *60 + time[1]
button = [600,60,30,10]
flag = False
button_click = 0

if time[1] == 30:
    time2 -= 30
    flag = True
    button_click += 1
for i in range(4):

    if time2 == 0:
        break
    x = time2 // button[i]
    time2 = time2 % button[i]
    if x >= 1 and i == 2:
        flag = True

    button_click += x

if not flag:
    button_click += 1

print(button_click)
