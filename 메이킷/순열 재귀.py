arr = [1,2,3,4,5]
visit = [False for _ in range(5)]

r = 3
def permutation(idx,depth):

    if depth == r:
        print(ret)
        return

    for i in range(len(arr)):
        if visit[i]:
            continue
        visit[i] = True
        ret[depth] = arr[i]
        permutation(idx+1,depth+1)
        visit[i] = False

    return
ret = [0 for _ in range(3)]
def combination(idx,cnt):

    if cnt == r:
        print(ret)
        return

    for i in range(idx,len(arr)):
        ret[cnt] = arr[i]
        combination(i+1,cnt+1)
    return


def permutation_repition(depth):

    if depth == r:
        print(ret)
        return

    for i in range(len(arr)):
        ret[depth] = arr[i]
        permutation_repition(depth+1)

    return




def combination_repition(idx,depth):

    if depth == r:
        print(ret)
        return

    for i in range(idx,len(arr)):
        ret[depth] = arr[i]
        combination_repition(i,depth+1)

    return

permutation(0,0)
