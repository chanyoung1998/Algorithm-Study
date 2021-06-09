import sys
from itertools import combinations
n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
numbers_1 = numbers[:n//2]
numbers_2 = numbers[n//2:]


def subsetsum(numbers):
    subsetsum = []
    for i in range(len(numbers)+1):
        for subsets in combinations(numbers,i):
            subsetsum.append(sum(subsets))
    return subsetsum

subsetsum_numbers1 = subsetsum(numbers_1)
subsetsum_numbers2 = subsetsum(numbers_2)
subsetsum_numbers2.sort()

dp = [False for _ in range(2000000)]
for x in subsetsum_numbers1:
    for y in subsetsum_numbers2:
        if dp[x+y] == False:
            dp[x+y] =True

for i in range(2000000):
    if not dp[i]:
        print(i)
        break

