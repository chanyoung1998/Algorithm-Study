T  = int(input())

for t in range(1,T+1):
    n,m = map(int,input().rstrip().split())
    A = set(input().rstrip().split())
    B = set(input().rstrip().split())
    print('#{} {}'.format(t,len(A.intersection(B))))