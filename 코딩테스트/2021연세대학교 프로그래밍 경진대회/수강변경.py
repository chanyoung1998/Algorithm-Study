import sys

n = int(sys.stdin.readline().rstrip())
cur_course = list(map(int,sys.stdin.readline().rstrip().split()))
wtc_course = list(map(int,sys.stdin.readline().rstrip().split()))
check = [0 for _ in range(1000001)]

for cur in cur_course:
    check[cur] += 1
for wtc in wtc_course:
    if check[wtc] > 0:
        check[wtc] -= 1

print(sum(check))