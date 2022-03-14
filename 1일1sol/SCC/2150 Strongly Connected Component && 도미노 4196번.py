import sys
sys.setrecursionlimit(100001)
def dfs(x):
    global ID,scc_cnt
    dfsn[x] = ID
    ID += 1
    stack.append(x)
    p = dfsn[x]
    for next in adj[x]:
        if dfsn[next] == -1:
            p = min(p,dfs(next))
        elif not finished[next]:
            p = min(p,dfsn[next])

    if p == dfsn[x]:
        scc = []
        while(1):
            t = stack.pop()
            finished[t] =True
            SN[t] = scc_cnt
            scc.append(t+1)
            if x == t:
                break
        SCC.append(scc)
        scc_cnt += 1
    return p
testcase = int(sys.stdin.readline().rstrip())

for _ in range(testcase):

    V,E = map(int,sys.stdin.readline().rstrip().split())
    adj = [[] for _ in range(V)]
    stack = []
    SCC = []
    scc_cnt = 0
    finished = [False for _ in range(V)]
    dfsn = [-1 for _ in range(V)]
    SN = [-1 for _ in range(V)]
    for _ in range(E):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        adj[a-1].append(b-1)
    ID =0
    for i in range(V):
        if dfsn[i] == -1:
            dfs(i)

    indegree = [0 for _ in range(len(SCC))]

    for cur in range(V):
        for next in adj[cur]:
            if SN[cur] != SN[next]:
                indegree[SN[next]] += 1

    ret = 0
    for x in indegree:
        if x == 0:
           ret += 1

    print(ret)




