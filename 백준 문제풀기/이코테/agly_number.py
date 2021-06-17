import sys
import heapq
n = int(sys.stdin.readline())
ugly = [0] * 1001


heap = [1]
count = 0

while count <= 1000:
    k = heapq.heappop(heap)
    if k == ugly[count-1]:
        continue
    ugly[count] = k
    count += 1

    heapq.heappush(heap,2 * k)
    heapq.heappush(heap,3 * k)
    heapq.heappush(heap,5 * k)

print(ugly[n-1])

