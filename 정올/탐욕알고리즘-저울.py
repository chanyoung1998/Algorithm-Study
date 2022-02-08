import sys

n = int(sys.stdin.readline().rstrip())
weights = list(map(int,sys.stdin.readline().rstrip().split()))
weights.sort()

check = 1
for i in range(n):
    if weights[i] <= check:
        check += weights[i]

print(check)