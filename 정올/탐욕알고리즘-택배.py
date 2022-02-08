import sys
# https://www.acmicpc.net/board/view/6327

n,c = map(int,sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline())
shipment = []
capacity = [c for _ in range(n)]
for _ in range(m):
    shipment.append(tuple(map(int,sys.stdin.readline().rstrip().split())))
shipment.sort(key=lambda x:(x[1],x[0]))

# print(shipment)
ret = 0
for i in range(m):

    start,end,weight = shipment[i]
    max_cap = min(capacity[start:end]) #start부터 end-1번 마을 까지 실을 수 있는 용량 중 최소
    max_weight = min(weight,max_cap)
    for j in range(start,end):
        capacity[j] -= max_weight

    ret += max_weight

print(ret)