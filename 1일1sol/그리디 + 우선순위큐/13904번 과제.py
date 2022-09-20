from sys import stdin
input = stdin.readline
import heapq

N=int(input())
arr = [None for i in range(N)]
for i in range(N):
    arr[i]=tuple(map(int,input().split()))

arr.sort()
hq=[]

for tp in arr:
    day = tp[0]
    heapq.heappush(hq,tp[1])
    if(len(hq)>day):
        heapq.heappop(hq)

print(sum(hq))
