import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    w = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    circle = []
    edge = []
    for _ in range(n):
        circle.append(tuple(map(int,sys.stdin.readline().rstrip().split())))

    

