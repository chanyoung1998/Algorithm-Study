'''
내용:백준 알고리즘 단계별 풀기 우선순위 큐 11066 최대 힙
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
        heapq.heappush(heap,(-x,x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)