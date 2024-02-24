import sys

#비둘기 집의 원리

n,r = map(int,sys.stdin.readline().rstrip().split())
print((n+1) + 2 * (r-1))