import sys


n = int(sys.stdin.readline().rstrip())
board = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
board.sort(key=lambda x:x[0])
