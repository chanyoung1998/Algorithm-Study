import sys




n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
log =[[] for _ in range(n+1)]
for i in range(1,n+1):
    inputs = list(map(int,sys.stdin.readline().rstrip().split()))

    for x in inputs:
        if x != i:
            graph[i].append(x)
        else:
            break
    graph[i].append(i)

v = n

stack = []
low = [-1] * (v + 1)
ids = [-1] * (v + 1)
visited = [0] * (v + 1)
idid = 0
result = []


def dfs(x, low, ids, visited, stack):
    global idid
    ids[x] = idid
    low[x] = idid
    idid += 1
    visited[x] = 1
    stack.append(x)

    for ne in graph[x]:
        if ids[ne] == -1:
            dfs(ne, low, ids, visited, stack)
            low[x] = min(low[x], low[ne])
        elif visited[ne] == 1:
            low[x] = min(low[x], ids[ne])

    w = -1
    scc = []
    if low[x] == ids[x]:
        while w != x:
            w = stack.pop()
            scc.append(w)
            visited[w] = -1
        result.append(sorted(scc))


for i in range(1, v + 1):
    if ids[i] == -1:
        dfs(i, low, ids, visited, stack)

for _ in range(len(result)):
    result[_] = set(result[_])

for i in range(1,n+1):
    flag = False
    for res in result:
        if flag:
            break
        if i in res:
            for next in graph[i]:
                if next in res:
                    print(next)
                    flag = True
                    break
        else:
            continue

    if not flag:
        print(i)












# def dfs(cur):
#
#
#     if visit[cur]:
#         return False
#
#     visit[cur] =True
#
#     for next in adjlist[cur]:
#
#         if matching[next] == -1:
#             matching[next] = cur
#             log[cur].append(next)
#             return True
#
#         elif dfs(next):
#             matching[next] = cur
#             log[cur].append(next)
#             return True
#
#
#     return False
#
# matching = [-1 for _ in range(n+1)]
# visit = [False for _ in range(n+1)]
#
# for i in range(1,n+1):
#     visit = [False for _ in range(n + 1)]
#     dfs(i)
#     # print(matching)
#
# ret = [0 for _ in range(n+1)]
# for i in range(1,n+1):
#     ret[matching[i]] = i
#
# for i in range(1,n+1):
#     print(ret[i])
#
# print(log)