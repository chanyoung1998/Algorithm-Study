s = 0
e = 9
a = [1,2,3,4,5,6,7,8,9,10]
t = 2

while s < e:
    m = (s+e)//2

    if a[m] < t:
        s = m+1
    else:
        e = m

print(a[s-1])