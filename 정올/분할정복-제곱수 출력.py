import sys
#해결법 (A*B)%C = ((A%C)*(B*C))%C
x,y = map(int,sys.stdin.readline().rstrip().split())
mod = 20091024
def sol(n,level):
    if level == 0:
        return 1
    elif level == 1:
        return n

    if level % 2 == 0:
        num = sol(n,level//2)
        return ((num%mod) * (num% mod)) % mod
    else:
        num = sol(n,level-1)
        return ((num%mod) * (n%mod)) %mod

print(sol(x,y))