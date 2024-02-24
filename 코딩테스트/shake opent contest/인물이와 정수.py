import sys
import heapq

n, m = map(int,sys.stdin.readline().rstrip().split())
difficulty = list(map(int,sys.stdin.readline().rstrip().split()))
p = int(sys.stdin.readline().rstrip())
tips = [[] for _ in range(n)]
for _ in range(p):
    a,b,t = map(int,sys.stdin.readline().rstrip().split())
    difficulty[b-1] += t
    tips[a-1].append((b-1,t))

heap = []
for i in range(n):
    heapq.heappush(heap,(difficulty[i],i))


ret = 0
count = 0
visit = [False for _ in range(n)]
while count < m:
    x = heapq.heappop(heap)
    if visit[x[1]]:
        continue

    visit[x[1]] = True
    count += 1
    ret = max(ret,x[0])
    for b,t in tips[x[1]]:
        difficulty[b] -= t
        heapq.heappush(heap,(difficulty[b],b))
print(ret)

