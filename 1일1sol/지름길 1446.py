import sys

n,d = map(int,sys.stdin.readline().strip().split(' '))
loads=[tuple(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(n)]
ret = sys.maxsize
loads.sort(key=lambda x: x[1])
def dfs(index, cur, distances):
    global ret

    if index == n:
        ret = min(ret,distances + d-cur)
        return

    if cur <= loads[index][0]:
        if loads[index][1] <= d and loads[index][1]-loads[index][0] > loads[index][2]:
            dfs(index+1,loads[index][1],distances + (loads[index][0]-cur) + loads[index][2])
            dfs(index+1, cur,distances)

        else:
            dfs(index+1, cur,distances)

    else:
        dfs(index+1,cur,distances)

dfs(0,0,0)
print(ret)