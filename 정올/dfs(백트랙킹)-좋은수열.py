N = int(input())

def check(n):
    n = list(str(n))
    length = len(n)
    for i in range(1,length//2 + 1):
        for j in range(length - 2 * i + 1):
            if n[j:j+i] == n[j+i:j+2*i]:
                return False


    return True

def dfs(cnt,num):
    if cnt == N:
        if check(num):
            print(num)
            exit(0)

        return

    if check(num):
        for i in [1,2,3]:
            dfs(cnt+1,num * 10 + i)

dfs(0,0)


