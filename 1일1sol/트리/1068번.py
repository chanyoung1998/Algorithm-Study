import sys

n = int(sys.stdin.readline())
parent = list(map(int,sys.stdin.readline().rstrip().split()))
remove = int(sys.stdin.readline())
print(parent)
def count_reaf(root):

    if root == remove:
        return 0
    count = 0
    flag = False
    for i in range(n):
        if parent[i] == root and i != remove:
            flag = True
            count += count_reaf(i)
    if not flag:
        count = 1

    return count
root = 0
for i in range(n):
    if parent[i] == -1:
        root = i
print(count_reaf(root))



