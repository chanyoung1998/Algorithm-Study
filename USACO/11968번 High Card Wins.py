import sys

n = int(sys.stdin.readline().rstrip())
elsie = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
elsie.sort()
count = n - 1
ret = 0
i = 2 * n
while count >= 0:

    if i in elsie:
        i -= 1
    elif i > elsie[count]:
        ret += 1
        count -= 1
        i -= 1
    else:
        count -= 1

print(ret)