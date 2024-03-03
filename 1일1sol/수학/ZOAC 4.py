import math

h,w,n,m = map(int,input().strip().split(' '))

a = math.rou(w / (1+m))
b = math.ceil(h / (1+n))

print(a * b)