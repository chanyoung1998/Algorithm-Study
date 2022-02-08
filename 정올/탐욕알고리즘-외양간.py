import sys

m,s,c = map(int,sys.stdin.readline().rstrip().split())
cows = [int(sys.stdin.readline()) for _ in range(c)]
cows.sort()
dist = []
for i in range(c-1):
    if cows[i] + 1 == cows[i+1]:
        continue
    else:
        dist.append(cows[i+1]-cows[i]-1)

dist.sort(reverse=True)

print((cows[-1]-cows[0]+1) -sum(dist[:m-1]))

