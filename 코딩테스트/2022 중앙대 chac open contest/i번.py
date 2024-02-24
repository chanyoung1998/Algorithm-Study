import sys

n,m,k = map(int,sys.stdin.readline().rstrip().split())

malhe = list(map(int,sys.stdin.readline().rstrip().split()))
no = list(map(int,sys.stdin.readline().rstrip().split()))

malhe.sort()
no.sort()

def binary(malhe_value,target):
    start = 0
    end = m

    while start < end:
        mid = (start + end )// 2
        if no[mid] ^ malhe_value:
            pass

