from heapq import heappop,heappush

T = int(input())
for t in range(1,T+1):
    n = int(input())
    heap = []
    ret = []
    for _ in range(n):
        inputs = input().rstrip().split()
        if len(inputs) == 2:
            heappush(heap,-int(inputs[1]))
        else:
            pop = 1
            if heap:
                pop = heappop(heap)

            ret.append(-pop)

    print('#{} '.format(t),end='')
    print(*ret)