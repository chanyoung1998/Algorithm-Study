import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    note,score = map(int,sys.stdin.readline().rstrip().split())
    if score - 1 % 5 != 0:
        print(-1)
        break