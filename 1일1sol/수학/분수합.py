import sys,math

a1,b1 = map(int,sys.stdin.readline().rstrip().split())
a2,b2 = map(int,sys.stdin.readline().rstrip().split())

LCM = math.lcm(b1,b2)
a1 = a1 * (LCM//b1)
a2 = a2 * (LCM//b2)

a3 = a1 + a2
GCD = math.gcd(a3, LCM)
print(a3//GCD, LCM//GCD)

