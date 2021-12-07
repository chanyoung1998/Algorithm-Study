
def comb(n,r,q):
    if r == 0:
        print(b[:q])
    elif n < r:
        return
    else:
        b[r-1] = a[n-1]
        comb(n-1,r-1,q)
        comb(n-1,r,q)

a = [1,2,3,4,5,6]
b= [0,0,0,0,0,0]
comb(6,4,4)