import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline())-1 for _ in range(n)]

visit = [False for _ in range(n)]
finish = [False for _ in range(n)]
ret = []
def dfs(curr):

    if not visit[curr]:
        visit[curr] = True

        next = arr[curr]

        if not visit[next]:
            dfs(next)
        else:
            if not finish[next]:
                temp = next
                ret.append(next)
                while temp != curr:
                    temp = arr[temp]
                    ret.append(temp)

    finish[curr] = True


for i in range(n):
    if not visit[i]:
        dfs(i)

# print(ret)
ret = list(set(ret))
print(len(ret))
ret.sort()


for i in ret:
    print(i+1)


