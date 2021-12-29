import sys
import heapq

c,n = map(int,sys.stdin.readline().rstrip().split())
chicken = [int(sys.stdin.readline()) for _ in range(c)]
cows = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
check = [False for _ in range(n)]

chicken.sort()
cows.sort(key=lambda x:(x[1],x[0]))
count = 0
for i in range(c):

    for j in range(n):
        if cows[j][0] <= chicken[i] <= cows[j][1] and not check[j]:
            check[j] = True
            count += 1
            break


print(count)




