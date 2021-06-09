import sys
import heapq
n = int(sys.stdin.readline())
card = []
for _ in range(n):
    heapq.heappush(card,int(sys.stdin.readline()))

sum = 0
for _ in range(n-1):
    a = heapq.heappop(card)
    b = heapq.heappop(card)

    sum += a + b
    heapq.heappush(card,a+b)

print(sum)