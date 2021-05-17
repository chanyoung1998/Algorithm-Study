import sys

n, k = map(int,sys.stdin.readline().rstrip().split())
food = list(map(int,sys.stdin.readline().rstrip().split()))
ret = -sys.maxsize
def sol(i,energy):
    global ret
    if i == n:
        ret = max(ret,energy)
        return
#count번부터 먹기 시작
    sum = 0
    count = 0
    for j in range(i,n):
        if sum >= k:
            break
        sum += food[j]
        count = j

    sol(count+1,energy+sum-k)
    sol(i+1,energy)

sol(0,0)
print(ret)

