import sys
k = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

ret = ''
for i in range(len(s)):
    if i % k == 0:
       ret += s[i]

print(ret)