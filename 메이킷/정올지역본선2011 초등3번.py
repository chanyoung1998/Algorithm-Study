import sys

n = int(sys.stdin.readline().rstrip())
flowers = []
start = 300
end = 301
maxend = 0
maxindex = 0
result = 0
for _ in range(n):
    inputs = list(map(int,sys.stdin.readline().rstrip().split()))
    flowers.append((inputs[0]*100+inputs[1],inputs[2]*100+inputs[3]))
flowers.sort()

