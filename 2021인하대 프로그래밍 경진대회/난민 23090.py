import sys
import heapq

n = int(sys.stdin.readline())
coord = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
maxq = []
minq = []
sum_x = 0

for x,y in coord:
    sum_x += abs(x)
    if len(maxq) == len(minq):
        heapq.heappush(maxq,-y)
    else:
        heapq.heappush(minq,y)

    if len(minq) == 0:

        print(-maxq[0],sum_x)
        continue

    if -maxq[0] < minq[0]:

        print(-maxq[0])
    elif -maxq[0] > minq[0]:
        temp_max = -heapq.heappop(maxq)
        temp_min = heapq.heappop(minq)
        heapq.heappush(maxq,-temp_min)
        heapq.heappush(minq,temp_max)
        print(-maxq[0])

                         








