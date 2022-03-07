import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
logs = [[i]+list(map(int,sys.stdin.readline().rstrip().split())) for i in range(n)]
logs.sort(key=lambda x:(x[1]))
link = [i for i in range(n)]
# print(logs)
end = logs[0][2]
for i in range(1,n):
    if logs[i][1] <= end:
        link[logs[i][0]] = link[logs[i-1][0]]
        end = max(end,logs[i][2])
    else:
        end = logs[i][2]

# print(link)


for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    if link[a-1] == link[b-1]:
        print(1)
    else:
        print(0)