import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
array = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
rvs = []
for s,e in array:
    if e < s:
        rvs.append((s,e))

# (4,2),(7,5),(8,1) m = 10인 경우가 반례임
# rvs.sort(key=lambda x:(x[0],x[1]))
rvs.sort(key=lambda x:-x[0])
ret = m
start = -1
end = -1
for i in range(len(rvs)):
    if start == -1 and end == -1:
        start = rvs[i][0]
        end = rvs[i][1]
    else:
        if rvs[i][0] < end:
            ret += 2 * (start-end)
            start = rvs[i][0]
            end = rvs[i][1]
        else:
            start = max(start,rvs[i][0])
            end = min(end,rvs[i][1])

print(ret + 2 * (start-end))
