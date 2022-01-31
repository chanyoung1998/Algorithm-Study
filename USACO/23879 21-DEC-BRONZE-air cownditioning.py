import sys

n = int(input())
p = list(map(int,input().rstrip().split()))
t = list(map(int,input().rstrip().split()))
diff = [p[i]-t[i] for i in range(n)]

ans = 0
i = 0
same= False
stack = []

while i < n:
    while i < n and diff[i] == 0:
        i += 1
        same = False

    if i == n:
        break

    j = i
    m = 1e4 + 1
    if not same:
        while j < n and diff[i] * diff[j] > 0:
            if abs(diff[j]) < m:
                stack.append((j,m-abs(diff[j])))
                m = abs(diff[j])
            j += 1
    else:
        j,m = stack.pop()

    for x in range(i,j):
        diff[x] += -m if diff[x] > 0 else m

    ans += m
    same = True

print(ans)

