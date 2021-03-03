'''
내용:백준 알고리즘 단계별 풀기 우선순위 큐 1655 가운데를 말해요
날짜:21년3월3일
사용 언어:파이썬
'''

import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
min_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-x, x))
    else:
        heapq.heappush(min_heap, (x, x))


    if min_heap and max_heap[0][1] > min_heap[0][1]:
        temp_max = heapq.heappop(max_heap)[1]
        temp_min = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-temp_min, temp_min))
        heapq.heappush(min_heap, (temp_max, temp_max))
    print(max_heap[0][1])








#시간 초과 발생
'''for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap,x)
    temp_heap = heap.copy()
    temp = []
    while temp_heap:
        temp.append(heapq.heappop(temp_heap))
    length = len(temp)
    if length % 2 == 0:
        print(min(temp[length//2], temp[length//2 - 1]))
    else:
        print(temp[length//2])'''

