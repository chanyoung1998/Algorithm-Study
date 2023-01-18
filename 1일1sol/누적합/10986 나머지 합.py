import sys

n,m = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
prefixSum = [0 for _ in range(n+1)]
mod = [0 for _ in range(m)]

for i in range(1,n+1):
    prefixSum[i] = (prefixSum[i-1] + A[i-1]) % m
    mod[prefixSum[i]] += 1

ret = 0
for i in range(m):
    ret += mod[i]*(mod[i]-1) / 2 + (mod[i] if i == 0 else 0)

print(int(ret))