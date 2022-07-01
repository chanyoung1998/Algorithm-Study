import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

check_row = [False for _ in range(n)]
check_col = [False for _ in range(n)]

