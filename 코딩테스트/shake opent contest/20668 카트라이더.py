import sys
import heapq

MOD = 3628800
n, m = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[] for _ in range(n+1)]
time = [[sys.maxsize for _ in range(11)] for _ in range(n+1)]
for _ in range(m):
    a,b,l,k = map(int,sys.stdin.readline().rstrip().split())
    adjlist[a].append((b,l * MOD ,k))
    adjlist[b].append((a,l * MOD,k))


def dijckstra():


    pq = [(0,1,1)]
    #(시간,노드번호,속도)

    time[1][1] = 0

    while pq:
        cur_time,cur_node,cur_speed = heapq.heappop(pq)
        if time[cur_node][cur_speed] < cur_time:
            continue

        for next_node,l,k in adjlist[cur_node]:

            for alpha in range(-1,2):
                next_speed = cur_speed + alpha
                if 1 <= next_speed <= k:
                    next_time = l / next_speed + cur_time
                    if time[next_node][next_speed] > next_time:
                        time[next_node][next_speed] = next_time
                        heapq.heappush(pq,(next_time,next_node,next_speed))
            # if cur_speed <= k and cur_time + l/cur_speed < time[next_node][cur_speed]:
            #     time[next_node][cur_speed] = cur_time + l/cur_speed
            #     pq.append((cur_time + l / cur_speed,next_node,cur_speed))
            # if cur_speed + 1 <= k and cur_time + l/(cur_speed+1) < time[next_node][cur_speed+1]:
            #     time[next_node][cur_speed+1] = cur_time + l / (cur_speed+1)
            #     pq.append((cur_time+l /(cur_speed+1), next_node,cur_speed+1))
            # if cur_speed - 1 >= 1 and cur_time + l / (cur_speed - 1) < time[next_node][cur_speed -1]:
            #     time[next_node][cur_speed - 1] = cur_time + l / (cur_speed - 1)
            #     pq.append((cur_time + l / (cur_speed - 1), next_node, cur_speed - 1))


dijckstra()
res = min(time[n])


print(int(res//MOD), end='')
print(('%.9f'%round((res % MOD)/MOD,9))[1:])
# print('%.9f' % round((res % MOD)/MOD,9))