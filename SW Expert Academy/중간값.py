from heapq import heappush,heappop

T = int(input())
mod = 20171109
for t in range(1,T+1):
    n, first = map(int,input().rstrip().split())
    min_heap = []
    max_heap = []
    heappush(max_heap,-first)
    ret = 0
    for _ in range(n):
        for num in list(map(int,input().rstrip().split())):
            if len(max_heap) == len(min_heap):
                heappush(max_heap,-num)
            else:
                heappush(min_heap,num)

            if min_heap and min_heap[0] < -max_heap[0]:
                max_pop = -heappop(max_heap)
                min_pop = heappop(min_heap)
                heappush(max_heap,-min_pop)
                heappush(min_heap,max_pop)
        # print(-max_heap[0])
        ret = (ret - max_heap[0]) % mod

    print('#{} {}'.format(t,ret % mod))