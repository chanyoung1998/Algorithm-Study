n = int(input())
coord = []
maps = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            maps[i][j] = 1

ret = 0
for _ in range(100):
    ret += sum(maps[_])
print(ret)
