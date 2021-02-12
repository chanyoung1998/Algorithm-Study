'''

정석적인 풀이로 풀면 시간 초과가 난다.
어쩔 수 없이 최악의 경우 O(2^N)이기 때문..
'''


n,k = map(int,input().split(' '))
arr = []
x = [0 for _ in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split(' '))))
#가성비 좋은 순서대로 정렬
arr.sort(key= lambda x:(x[1]/x[0]),reverse= True)

#arr[cnt]가 들어갈지 말지 결정, 현재 배낭의 크기 size
MP = 0

def Knapsack(cnt,size):
    global MP
    P = 0
    S = 0
    for i in range(n):
        if x[i] == 1:
            P += arr[i][1]
            S += arr[i][0]

    if cnt >= n or size <= 0:
        MP = max(MP,P)
        return

    #현재 들어가 있는 물건의 가치의 합과 무게의 합


    if arr[cnt][0] <= size:
        B = fractional(cnt+1,size-arr[cnt][0])
        if MP < P + arr[cnt][1] + B:
            x[cnt] = 1
            Knapsack(cnt+1,size-arr[cnt][0])


    B = fractional(cnt+1,size)
    if MP < P + B:
        x[cnt] = 0
        Knapsack(cnt+1,size)

def fractional(cnt,size):
    B = 0
    S = size
    for i in range(cnt,n):
        if arr[cnt][0] <= S:
            B += arr[cnt][1]
            S -= arr[cnt][0]
        else:
            temp = 0
            while arr[cnt][0] >= temp and S >= 0:
                temp += 1
                B += arr[cnt][1]/arr[cnt][0]
                S -= 1

    return B

Knapsack(0,k)
print(MP)


