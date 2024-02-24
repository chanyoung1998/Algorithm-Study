import sys
from collections import deque
n,m = map(int,sys.stdin.readline().rstrip().split())
station = list(map(int,sys.stdin.readline().rstrip().split()))
index = [0 for _ in range(5000001)]
dq = deque(station)



for _ in range(m):
    inputs = list(sys.stdin.readline().rstrip().split())
    cmd = inputs[0]
    if cmd == "BN":
        circular.BN(int(inputs[1]),int(inputs[2]))
    elif cmd == 'BP':
        circular.BP(int(inputs[1]),int(inputs[2]))
    elif cmd == "CN":
        circular.CN(int(inputs[1]))
    elif cmd == "CP":
        circular.CP(int(inputs[1]))
