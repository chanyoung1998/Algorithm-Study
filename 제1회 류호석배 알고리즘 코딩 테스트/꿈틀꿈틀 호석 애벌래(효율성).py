import sys

n, k = map(int,sys.stdin.readline().rstrip().split())
food = list(map(int,sys.stdin.readline().rstrip().split()))
memorization = [0 for _ in range(n+1)]



def sol(i):
    if i == n:
        return 0
    if memorization[i] != 0:
        return memorization[i]
    else:
        sum = 0
        count = 0
        for j in range(i, n):
            if sum >= k:
                break
            sum += food[j]
            count = j

        memorization[i] = sol(count+1) + sum-k
        memorization[i] = max(sol(i+1), memorization[i])
        return memorization[i]


sol(0)
print(memorization[0])
