import heapq

heap = []
heapq.heappush(heap,(1,'1'))
heapq.heappush(heap,(3,'3'))
heapq.heappush(heap,(2,'2'))
print(heap)
heapq.heapreplace(heap,(5,'1'))
print(heapq.heappop(heap))