import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
adjlist = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            adjlist[i][j] = min(adjlist[i][j],adjlist[i][k] + adjlist[k][j])



for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    a,b = a-1,b-1
    if adjlist[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")