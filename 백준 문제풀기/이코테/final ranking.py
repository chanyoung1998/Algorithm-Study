import sys
from itertools import combinations
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    prev_ranking = list(map(lambda x:x-1,map(int,sys.stdin.readline().rstrip().split())))
    m = int(sys.stdin.readline())
    changed_ranking = []
    none_changed_ranking = []
    indegree = [0 for _ in range(n)]

    for _ in range(m):
        a, b = map(lambda x:x-1,map(int,sys.stdin.readline().rstrip().split()))
        changed_ranking.append((a,b))
        if prev_ranking.index(a) > prev_ranking.index(b):
            indegree[b] += 1
        else:
            indegree[a] += 1


    for x,y in combinations(range(n),2):
        if (x,y) not in changed_ranking:
            none_changed_ranking.append((x,y))
            if prev_ranking.index(x) < prev_ranking.index(y):
                indegree[y] += 1
            else:
                indegree[x] += 1


