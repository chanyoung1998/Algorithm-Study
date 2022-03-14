n = int(input())
def hanoi(x,a,b):
    if x == 0:
        return
    c  = 3 -(a+b)
    hanoi(x-1,a,c)
    print(x,':',a+1,'->',b+1)
    hanoi(x-1,c,b)

hanoi(n,0,2)