# import sys

T = int(input())
for t in range(T):
    n = int(input())


    check = 0
    cnt = 1
    a = n
    while check != 2 ** 10 - 1:
        temp = a * cnt
        for s in str(temp):
            if not (check & 1 << int(s)):
                check = check | 1 << int(s)
        cnt += 1
    print("#",t+1,' ',temp,sep='')
