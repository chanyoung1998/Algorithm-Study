for t in range(1,11):
    n = int(input())
    ret = -1
    for _ in range(n):
        inputs = input().rstrip().split()
        if len(inputs) == 4:
            if inputs[1].isdigit():
                ret = 0
        elif len(inputs) == 2:
            if not inputs[1].isdigit():
                ret = 0
    if ret == -1:
        ret = 1

    print('#{} {}'.format(t,ret))
