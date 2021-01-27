'''
내용:백준 알고리즘 단계별 풀기 백트래킹 15652 N과 M(4)
날짜:21년1월27일
사용 언어:파이썬
'''

n,m = map(int,input().split())
x = [0 for _ in range(m)]

def sol(cnt):
    if cnt == m:
        print(*x)
        return

    for i in range(1,n+1):
        if cnt == 0:
            x[cnt] = i
            sol(cnt+1)
        else:
            if max(x) <= i:
                x[cnt] = i
                sol(cnt+1)
                x[cnt] = 0



sol(0)