import sys

joker = 1
newjoker = 1


for i in range(int(sys.stdin.readline().rstrip())):
    inputs = list(map(int,sys.stdin.readline().rstrip().split()))
    joker = newjoker
    newjoker = 0

    if joker <= 13:
        left = True
        right = False
    else:
        joker -= 13
        left = False
        right = True

    for j in range(len(inputs)):
        if left:
            if j % 2 == 0:
                newjoker += inputs[j]
            else:
                joker -= inputs[j]
                if joker <= 0:
                    newjoker += inputs[j]
                    newjoker += joker
                    break
                else:
                    newjoker += inputs[j]
        else:
            if j % 2 == 1:
                newjoker += inputs[j]
            else:
                joker -= inputs[j]
                if joker <= 0:
                    newjoker += inputs[j]
                    newjoker += joker
                    break
                else:
                    newjoker += inputs[j]



print(newjoker)