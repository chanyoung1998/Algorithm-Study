import sys
import heapq

#그리디로도 풀 수 있음

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


n = int(sys.stdin.readline())
temp_p_and_d = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
temp_p_and_d.sort(key=lambda x:(-x[1],-x[0]))
p_and_d = []
parent = [i for i in range(10001)]
for payment, day in temp_p_and_d:
    heapq.heappush(p_and_d,(-payment,day))

ret = 0
while p_and_d:
    payment, day = heapq.heappop(p_and_d)
    payment = -payment
    p = find(day)
    if p == 0:
        continue
    else:
        parent[p] = p-1
        ret += payment

print(ret)