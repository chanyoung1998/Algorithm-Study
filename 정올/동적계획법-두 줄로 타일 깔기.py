import sys

n =int(sys.stdin.readline())
# an = a(n-1) + 2 * a(n-2)
mod = 20100529
a1 = 1
a2 = 3
if n >= 3:
    for i in range(3,n+1):
        tmp = a2
        a2 = (a2 + 2 * a1) % mod
        a1 = tmp
    print(a2)
elif n == 2:
    print(a2)
else:
    print(a1)