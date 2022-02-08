import sys
#해결방법: 주머니에 있는 총 동전의 합에서 w를 빼준 만큼을 일단 가능한 단위가 큰 동전으로 먼저 거슬러 준다(즉, 최소의 개수로 거슬러 준다)
# 그 다음 원래 코인 개수에서 거슬러 준 코인 개수를 빼주면 w를 최대로 많이 거슬러 준 경우가 된다

w = int(sys.stdin.readline().rstrip())
#현재 주머니에 있는 코인 개수
counts = list(map(int,sys.stdin.readline().rstrip().split()))
coins = [500,100,50,10,5,1]
#거슬러 준 코인의 개수
table = [0 for _ in range(6)]

#총 주머니에 있는 돈의 합
sum_= 0
for i in range(6):
    sum_ += counts[i] * coins[i]

# 총 돈의 합- w
w = sum_ - w
#(총 돈의 합 - w)을 최소한의 개수로 거슬러 줘야하는 개수 구하기
for i in range(6):
    table[i] = min(w//coins[i],counts[i])
    w -= coins[i] * table[i]

for i in range(6):
    counts[i] -= table[i]

print(sum(counts))
print(*counts)

