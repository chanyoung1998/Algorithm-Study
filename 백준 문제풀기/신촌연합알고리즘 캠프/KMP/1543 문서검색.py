import sys

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

count = []
for i in range(len(s)-len(p)+1):
    for j in range(len(p)):
        if s[i+j] == p[j]:
            if j == len(p)-1:
                count.append(i)
        else:
            break

ret = 0
r = 0
for i in count:
    if ret <= i:
        ret = i + len(p)
        r += 1
print(r)