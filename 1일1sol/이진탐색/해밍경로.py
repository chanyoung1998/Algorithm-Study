import sys
import heapq

n,k = map(int,sys.stdin.readline().rstrip().split())
binary_codes = [(i,sys.stdin.readline().rstrip())for i in range(n)]
binary_codes.sort(key=lambda x:x[1])
m = int(sys.stdin.readline().rstrip())
adjlist = [[] for _ in range(n)]
def hamming_distance(node,number):
    for i in range(k):
        target = ''
        for j in range(k):
            if i == j:
                if node[j] == '0':
                    target += '1'
                else:
                    target += '0'
            else:
                target += node[j]

        start = -1
        end = n
        flag = False
        while start + 1 < end:
            mid = (start+end) // 2

            if target == binary_codes[mid][1]:
                flag = True
                break
            elif target > binary_codes[mid][1]:
                start = mid
            else:
                end = mid
        if flag:
            adjlist[number].append(binary_codes[mid][0])

def dijkstra(start):

    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0

    while q:
        now,dist = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in adjlist[now]:
            if distance[i] > dist + 1:
                distance[i] = dist + 1
                path[i] = now
                heapq.heappush(q, (i, dist + 1))

for i in range(n):
    hamming_distance(binary_codes[i][1],binary_codes[i][0])

path = [-1 for _ in range(n)]
distance = [sys.maxsize for _ in range(n)]
dijckstra(0)
'''print(adjlist)
print(distance)
print(path)'''
for _ in range(m):
    end = int(sys.stdin.readline())
    if distance[end-1] != sys.maxsize:
        ret = [end]
        next = end-1
        while path[next] != 0:
            ret.append(path[next]+1)
            next = path[next]

        ret.append(1)
        print(*ret[::-1])
    else:
        print(-1)





