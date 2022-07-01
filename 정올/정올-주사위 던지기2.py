import sys

n ,m = map(int,sys.stdin.readline().rstrip().split())
ret = [-1 for _ in range(n)]

def function(cnt,sum):
    if cnt == n:
        if sum == m:
            print(*ret)

        return

    for i in range(1,7):
        ret[cnt] = i
        if sum+i > m:
            return
        function(cnt+1,sum+i)

function(0,0)