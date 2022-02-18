from itertools import permutations,combinations

array = [1,1,1,2]
visit = [False for _ in range(4)]
for per in permutations(array):
    print(list(per))

#nPr
def per(cnt,num,n,r):
    if cnt == r:
        print(num)
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            per(cnt+1,num * 10 + array[i],n,4)
            visit[i] = False

per(0,0,4,3)

