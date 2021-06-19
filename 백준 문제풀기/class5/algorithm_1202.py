import sys
import heapq

n, k = map(int,sys.stdin.readline().rstrip().split())
jewelly = []
bag = []
for _ in range(n):
    weight, value = map(int,sys.stdin.readline().rstrip().split())
    jewelly.append((weight,value))
for _ in range(k):
    bag.append(int(sys.stdin.readline()))

jewelly.sort(key=lambda x:x[0])
bag.sort()

ret = 0
i = 0
q = []
# 가방에 들어갈 수 있는 보석 들 중 가치가 가장 높은 것 뽑기
# 가방무게가 오름 차순이기 때문에 우선순위 큐에 있는 root를 pop만 하면 된다
for bag_weight in bag:

    while i < n:
        if bag_weight >= jewelly[i][0]:
            heapq.heappush(q,(-jewelly[i][1],jewelly[i][0]))
        else:
            break
        i += 1
    if q:
        root = heapq.heappop(q)
        ret += root[0]
print(-ret)


