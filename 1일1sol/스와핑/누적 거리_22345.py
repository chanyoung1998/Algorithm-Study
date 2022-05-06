import sys

n,q = map(int,sys.stdin.readline().rstrip().split())
village = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
Q = [(int(sys.stdin.readline().rstrip()),_) for _ in range(q)]
result = [0 for _ in range(q)]
Q.sort(key=lambda x:x[0])
village.sort(key=lambda x:x[1])
people = 0
distance_sum = 0
t = 0
temp = 0
for j in range(n):
    if village[j][1] <= Q[0][0]:
        t = j
        temp += village[j][0]
        if j == n-1:
            t = n
    people += village[j][0]
    distance_sum += abs(Q[0][0]-village[j][1]) * village[j][0]
result[Q[0][1]] = distance_sum
# print(distance_sum)

cnt_1 = temp # 스와핑 하면서 지나간 마을 -> 이 마을들에 대해서는 점점 멀어짐
cnt_2 = people-temp # 스와핑 하면서 아직 안 지나간 마을 -> 이 마을들에 대해서는 점점 가까워짐

i = 1 #회의 장소 idx
j = t #마을 idx

while i < q:
    temp = 0

    for x in range(j,n):
        if village[x][1] <= Q[i][0]:
            distance_sum += village[x][0] * (Q[i][0] - village[x][1])  - village[x][0] * (village[x][1] - Q[i-1][0])
            temp += village[x][0]
            cnt_2 -= village[x][0]
            if x == n -1:
                j = n
                break

        else:
            j = x
            break

    distance_sum += cnt_1 * (Q[i][0]-Q[i-1][0]) - cnt_2 * (Q[i][0]-Q[i-1][0])
    cnt_1 += temp

    result[Q[i][1]] = distance_sum
    # print(distance_sum)

    i += 1


for _ in range(q):
    print(result[_])