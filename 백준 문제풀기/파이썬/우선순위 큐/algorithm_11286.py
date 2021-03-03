'''
내용:백준 알고리즘 단계별 풀기 우선순위 큐 11286 절댓값 힙
날짜:21년3월3일
사용 언어:파이썬
'''
import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(heap,(abs(x),x))
    else:
        if heap:
            t = heap[0][1]
            temp = []
            while heap and abs(t) == heap[0][0]:
                t = heapq.heappop(heap)[1]
                heapq.heappush(temp, t)

            print(heapq.heappop(temp))
            while temp:
                s = heapq.heappop(temp)
                heapq.heappush(heap, (abs(s), s))
        else:
            print(0)
