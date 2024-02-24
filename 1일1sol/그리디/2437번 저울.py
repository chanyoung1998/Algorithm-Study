import sys
n = int(sys.stdin.readline())
weights = list(map(int,sys.stdin.readline().rstrip().split()))
weights.sort()

x = 0
for i in range(n):
    if x+1 >= weights[i]:
        x += weights[i]
    else:
        break

print(x+1)