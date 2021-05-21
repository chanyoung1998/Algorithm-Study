import sys

n, k = map(int,sys.stdin.readline().rstrip().split())
food = list(map(int,sys.stdin.readline().rstrip().split()))
memorization = [0 for _ in range(n+1)]



'''def sol(i):
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
'''


'''sum = 0
l = 0
for r in range(1,n+1):
    sum += food[r-1]
    memorization[r] = memorization[r-1]
    while sum >= k:
        memorization[r] = max(memorization[r],memorization[l] + sum -k)
        sum -= food[l]
        l += 1

print(memorization[n])'''
sum = 0
start = 0
for end in range(1,n+1):
    sum += food[end-1]
    memorization[end] = memorization[end-1]
    while True:
        if sum >= k:
            memorization[end] = max(memorization[end],memorization[start] + sum - k)
            sum -= food[start]
            start += 1
        else:
            break
print(memorization)