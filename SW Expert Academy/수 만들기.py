
from heapq import heappop,heappush

T = int(input())

for t in range(1,T+1):
    n = int(input())
    A_list = list(map(int,input().rstrip().split()))
    K = int(input())
    X = K
    D = 1

    heap = []
    heappush(heap,(0,X))
    # dq = deque()
    # dq.append((X,0))

    while heap:
        cur_cnt,cur_x = heappop(heap)
        if cur_x == 0:
            print('#{} {}'.format(t,cur_cnt))
            break
        for A in A_list:
            heappush(heap,(cur_cnt + cur_x % A, cur_x // A))

