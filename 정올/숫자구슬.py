import sys

def check(mid):
    sum = 0
    groupcount = 1
    for i in range(n):
        sum += marbles[i]
        if sum > mid:
            groupcount += 1
            sum = marbles[i]

    return groupcount <= M


n,M = map(int,sys.stdin.readline().rstrip().split())
marbles = list(map(int,sys.stdin.readline().rstrip().split()))
left = max(marbles)-1
right = sum(marbles)

while left+1 < right:
    mid = (left+right) // 2

    if check(mid):
        right = mid
    else:
        left = mid


print(right)



