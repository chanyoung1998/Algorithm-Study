import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))

end = 0
sub_sum = 0
count = 0

for start in range(n):

    while sub_sum < m and end < n:
        sub_sum += array[end]
        end += 1

    if sub_sum == m:
        count += 1

    sub_sum -= array[start]

print(count)