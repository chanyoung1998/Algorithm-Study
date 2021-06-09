import sys


def lower_bound(array, k):
    start = 0
    end = len(array)-1

    while start < end:
        mid = (start+end)//2

        if array[mid] >= k:
            end = mid
        else:
            start = mid + 1

    return end


n = int(input())
array = list(map(int,input().split()))
ret = [-sys.maxsize]
count = 0
x = 0
dp = [0 for _ in range(n+1)]

for x in range(len(array)):
    if ret[-1] < array[x]:
        ret.append(array[x])
        count += 1
        dp[x] = count
    else:
        dp[x] = lower_bound(ret,array[x])
        ret[dp[x]] = array[x]

print(count)

res = []
max_val = count
for i in range(n, -1, -1):
    if dp[i] == max_val:
        res.append(array[i])
        max_val -= 1
res.reverse()
print(*res)