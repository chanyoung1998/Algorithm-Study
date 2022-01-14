import sys

na,nb = map(int,sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline())
adjlist = [[] for _ in range(na)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())

    adjlist[a-1].append(b-1)

if na % 2 == 0 and nb % 2 == 0:
    print(na//2 + nb//2)
elif na % 2 == 1 and nb% 2== 1:
    flag = False
    for i in range(na):
        if i % 2 == 1:
            continue
        for j in adjlist[i]:
            if j % 2 == 0:
                flag = True
                break

    if flag:
        print((na+nb)//2)
    else:
        print(na//2 + nb//2)
else:
    print(na//2 + nb//2)