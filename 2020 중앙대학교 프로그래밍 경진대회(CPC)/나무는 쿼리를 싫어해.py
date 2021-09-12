import sys

n = int(sys.stdin.readline())
query_1 = []
query_2 = []
for _ in range(n):
    a,i,j,k = map(int,sys.stdin.readline().rstrip().split())
    if a == 1:
        query_1.append((a,i,j,k))
    else:
        query_2.append((a,i,j,k))

query_2.sort(key=lambda x:x[3])
print(query_1)
print(query_2)

class Node:
    def __init__(self):
        self.lc = None
        self.rc = None
        self.value = 0


