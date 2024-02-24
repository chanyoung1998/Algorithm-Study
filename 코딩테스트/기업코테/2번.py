
# 돈 x원을 가지고 물감을 사려고 한다. cost[i]가 주어 지고 ith 번째 물감은 딱 2^i 개 만큼만  살 수 있다. 최대로 몇 개를 살 수 있는가
def solution(cost,x):
    n = len(cost)
    count = 0
    for i in range(n-1,-1,-1):
        if cost[i] <= x:
            x -= cost[i]
            count = (count + (1 << i)) % (10**9 + 7)

    return count

