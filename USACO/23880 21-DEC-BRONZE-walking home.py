import sys
dx = [0,1]
dy = [1,0]



def dfs(maps,i,j,dir,k):
    global K,N,count

    if k > K or maps[i][j] == 'H':
        return

    if i == N-1 and j == N-1 and k <= K:
        # print(i,j,k,path)
        count += 1
        return
    for x in range(2):
        p = i + dx[x]
        q = j + dy[x]
        if 0 <= p < N and 0 <= q < N and maps[p][q] != 'H':
            if dir == x:
                dfs(maps,p,q,x,k)
            else:

                dfs(maps,p,q,x,k+1)










for _ in range(int(sys.stdin.readline().rstrip())):
    N,K= map(int,sys.stdin.readline().rstrip().split())
    MAP = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    count = 0
    dfs(MAP,0,1,0,0,)
    dfs(MAP,1,0,1,0,)
    print(count)