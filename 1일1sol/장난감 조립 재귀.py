import sys

n =int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
part = [[0 for _ in range(n+1)] for _ in range(n+1)]
cnt = [0 for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
basic_part = set()

for _ in range(m):
    x,y,k = map(int,sys.stdin.readline().rstrip().split())
    part[x][y] = k
    indegree[x] += 1

for i in range(1,n+1):
    if indegree[i] == 0:
        basic_part.add(i)


def recur(num,k):

    if num in basic_part:
        cnt[num] += k
        return
    for i in range(1,n+1):

        if part[num][i] != 0:
            recur(i,part[num][i]*k)



recur(n,1)
for i in range(1,n+1):
    if i in basic_part:
        print(i,cnt[i])
