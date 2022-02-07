import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
# board = [[0 for _ in range(m)] for _ in range(n)]
k = int(sys.stdin.readline())
temp = 0
check = [False for _ in range(m)]
for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    temp = max(temp,a)
    a = n-a
    b -= 1
    check[b] = True
    # board[a][b] = 1

def search(mid):
    a = 0
    cnt = 0
    while a < m:
        if check[a]:
            a += mid
            cnt += 1
        else:
            a += 1

    return cnt <= k

left = temp-1
right = min(n,m)

while left + 1 < right:
    mid = (left+right) // 2

    if search(mid):
        right = mid
    else:
        left = mid


print(right)