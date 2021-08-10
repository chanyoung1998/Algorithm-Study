import sys

n = int(sys.stdin.readline())
points = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
points.sort(key=lambda x:x[0])

start_point = points[0][0]
end_point = points[0][1]
sumoflength = 0
for i in range(1,n):
    if points[i][0] < end_point and end_point < points[i][1]:
        end_point = points[i][1]
    elif start_point < points[i][0] and end_point < points[i][1]:
        sumoflength += end_point-start_point

        start_point = points[i][0]
        end_point = points[i][1]

sumoflength += end_point-start_point
print(sumoflength)