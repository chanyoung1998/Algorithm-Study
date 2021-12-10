import sys

n = int(sys.stdin.readline().rstrip())
radius = list(map(int,sys.stdin.readline().rstrip().split()))
coord_x = [0 for _ in range(n)]
coord_x[0] = radius[0]
for i in range(1,n):
    coord_x[i] = radius[i]
    for j in range(i):
        coord_x[i] = max(coord_x[i], coord_x[j] + 2 *((radius[i]*radius[j]) ** 0.5))


ans = 0
for i in range(n):
    ans = max(ans,radius[i] +coord_x[i])
print(ans)
