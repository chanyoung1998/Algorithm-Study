'''
24-08-11
프로그래머스
도넛과 막대 그래프

'''

import sys
from collections import defaultdict



def solution2(edges):
    answer = [0, 0, 0, 0]

    adjlist = defaultdict(list)
    node = set()
    for edge in edges:
        u = edge[0]
        v = edge[1]
        adjlist[u].append(v)
        node.add(u)
        node.add(v)

    passNode = set()
    stick = set()
    for n in node:
        if n not in passNode:
            visit = defaultdict(int)
            dfs(n, adjlist, visit, n)

            maxEdgeCnt = 0
            edgeCnt = 0
            nodeCnt = 0
            for k in visit.keys():
                nodeCnt += 1
                edgeCnt += visit[k]
                maxEdgeCnt = max(maxEdgeCnt,visit[k])

            ch = check(edgeCnt,nodeCnt,maxEdgeCnt)
            if ch == 1:
                passNode |= set(visit.keys())
                answer[1] += 1
            elif ch == 2:
                if all(v not in stick for v in visit.keys()):
                    answer[2] += 1
                    stick |= set(visit.keys())
            elif ch == 3:
                passNode |= set(visit.keys())
                answer[3] += 1
            else:
                answer[0] = n
    return answer

def dfs(cur, adjlist, visit, start):
    if visit[cur] == 0:
        for next in adjlist[cur]:
            visit[cur] += 1
            dfs(next, adjlist, visit, start)



def check(edgeCnt, nodeCnt, maxEdgeCnt):
    if nodeCnt == edgeCnt and maxEdgeCnt == 1:
        return 1
    elif nodeCnt - 1 == edgeCnt and maxEdgeCnt <= 1:
        return 2
    elif nodeCnt + 1 == edgeCnt and maxEdgeCnt == 2:
        return 3
    else:
        return -1

def solution(edges):
    answer = [0, 0, 0, 0]
    parent = {}
    outdegree = defaultdict(int)
    indegree = defaultdict(int)
    node = set()
    for edge in edges:
        u = edge[0]
        v = edge[1]
        outdegree[u] += 1
        indegree[v] += 1
        node.add(u)
        node.add(v)
        parent[u] = u
        parent[v] = v

    for n in node:
        if indegree[n] == 0 and outdegree[n] >= 2:
            answer[0] = n
            break

    for edge in edges:
        u = edge[0]
        v = edge[1]
        if u != answer[0]:
            union(u,v,parent)

    edgeCnt = defaultdict(int)
    nodeCnt = defaultdict(int)
    maxCnt = defaultdict(int)
    for n in node:
        if n == answer[0]:
            continue
        p = find(n,parent)
        edgeCnt[p] += outdegree[n]
        nodeCnt[p] += 1
        maxCnt[p] = max(maxCnt[p],outdegree[n])

    for p in edgeCnt.keys():
        ch = check(edgeCnt[p],nodeCnt[p],maxCnt[p])
        if ch == 1:
            answer[1] += 1
        elif ch == 2:
            answer[2] += 1
        elif ch == 3:
            answer[3] += 1

    print(answer)

    return answer

def union(a,b,parent):

    a = find(a,parent)
    b = find(b,parent)

    if a > b:
        a,b = b,a

    parent[b] = a

def find(a,parent):
    if parent[a] == a:
        return a

    parent[a] = find(parent[a],parent)
    return parent[a]


assert solution(
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]	) == [2, 1, 1, 0]
