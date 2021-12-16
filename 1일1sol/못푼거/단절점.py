import sys
sys.setrecursionlimit(10**6)

def dfs(node,isRoot):
    global counter
    visit_order[node] = counter
    ret = visit_order[node]
    counter += 1
    child = 0
    for next in adjlist[node]:
        if visit_order[next]:
            ret = min(ret,visit_order[next])
            continue

        prev = dfs(next,False)
        child += 1
        if not isRoot and prev >= visit_order[node]:
            isCut[node] = True

        ret = min(ret,prev)

    if isRoot:
        if child >= 2:
            isCut[node] = True

    return ret




v,e = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(v+1)]


for _ in range(e):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

isCut = [False for _ in range(v + 1)]
visit_order = [None for _ in range(v+1)]
counter = 1


for i in range(1,v+1):
    if not visit_order[i]:
        dfs(i,True)

cnt = 0
cut_ret = []
for i in range(1,v+1):
    if isCut[i]:
       cnt += 1
       cut_ret.append(i)

print(cnt)
print(*cut_ret)





