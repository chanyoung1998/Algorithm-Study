import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int,sys.stdin.readline().strip().split(' ')))
sensors.sort()
distances = []
for i in range(n-1):
    distances.append(sensors[i+1]-sensors[i])

distances.sort(reverse=True)

print(sum(distances) - sum(distances[:k-1]))
