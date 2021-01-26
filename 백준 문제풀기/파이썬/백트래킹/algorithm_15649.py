'''
내용:백준 알고리즘 단계별 풀기 백트래킹 15649 N과 M(1)
날짜:21년1월26일
사용 언어:파이썬
'''



n,m = map(int,input().split(' '))
visited = [False for _ in range(n+1)]
nums = [i for i in range(1,n+1)]
arr = []


def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in nums:
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(cnt+1)
            visited[i] = False
            arr.pop()



dfs(0)

