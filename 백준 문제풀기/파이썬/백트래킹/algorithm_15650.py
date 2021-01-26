'''
내용:백준 알고리즘 단계별 풀기 백트래킹 15650 N과 M(2)
날짜:21년1월26일
사용 언어:파이썬
'''

n,m = map(int,input().split())
visited = [False for i in range(n+1)]
arr = [0 for _ in range(m)]

def sol(cnt):
    if cnt == m:
        print(*arr)
        arr[cnt-1] = 0
        return

    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            if arr[cnt] < i:
                arr[cnt] = i
                sol(cnt + 1)
                visited[i] = False




sol(0)
