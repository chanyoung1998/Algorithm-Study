import sys
sys.setrecursionlimit(10**6)


def dfs(node,parent):

    global counter
    visit_order[node] = counter
    ret = visit_order[node]
    counter += 1
    for next in adjlist[node]:

        if next == parent:
            continue

        if visit_order[next]:
            ret = min(ret,visit_order[next])
            continue

        low = dfs(next,node)

        if low > visit_order[node]:
            edge.append((min(node,next),max(node,next)))
        ret = min(ret,low)

    return ret



v,e = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(v+1)]
visit_order = [None for _ in range(v+1)]
counter = 1
edge = []

for _ in range(e):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append(b)
    adjlist[b].append(a)


dfs(1,0)
edge.sort(key=lambda x:(x[0],x[1]))
print(len(edge))
for a,b in edge:
    print(a,b)