for t in range(int(input())):
    n,p = map(int,input().rstrip().split())
    study = list(map(int,input().rstrip().split()))
    table = [False for _ in range(1000001)]
    for day in study:
        table[day] = True

    ret = 0
    cnt = 0
    end = 0
    for start in range(1000001):

        while end < 1000001 and p > 0:
            if not table[end]:
                p -= 1
            end += 1

        if p == 0:
            while end < 1000001 and table[end]:
                end += 1

        ret = max(ret,end-start)

        if not table[start]:
            p += 1


    print('#{} {}'.format(t+1,ret))


