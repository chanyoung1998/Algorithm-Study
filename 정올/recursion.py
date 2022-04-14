import sys

array = list(map(int,sys.stdin.readline().rstrip().split()))
n = len(array)
k = int(sys.stdin.readline())
comb = [0 for _ in range(k)]
def func(idx,cnt):
    if cnt == k:
        print(comb)
        return

    else:
        for i in range(idx,n):
            comb[cnt] = array[i]
            func(i+1,cnt+1)

func(0,0)