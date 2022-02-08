import sys

n,s = map(int,sys.stdin.readline().rstrip().split())
inputs = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

i = 0
cost = 0
while i < n:
    cost += inputs[i][0] * inputs[i][1]
    j = i+1
    while j < n and inputs[i][0] + s * (j-i) < inputs[j][0] :
        cost += (inputs[i][0]+s*(j-i)) * inputs[j][1]
        j += 1
    i = j

print(cost)