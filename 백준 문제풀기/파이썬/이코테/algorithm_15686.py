import sys
from itertools import combinations

n, m = map(int,sys.stdin.readline().rstrip().split())
map = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
chicken = []
house = []

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            house.append((i,j))
        elif map[i][j] == 2:
            chicken.append((i,j))
ret = sys.maxsize
for chicken_max in combinations(chicken,m):
    city_ch_distance = 0
    for x,y in house:
        ch_distance = sys.maxsize
        for i,j in chicken_max:
            ch_distance = min(ch_distance,abs(x-i)+abs(y-j))
        city_ch_distance += ch_distance

    ret = min(ret,city_ch_distance)

print(ret)