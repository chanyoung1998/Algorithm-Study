'''
내용:백준 알고리즘 단계별 풀기 백트래킹 15651 N과 M(3)
날짜:21년1월27일
사용 언어:파이썬
'''


n,m = map(int,input().split())
x = [0 for _ in range(m)]


def sol(cnt):
    if cnt == m:
        print(*x)
        return

    for i in range(n):
        x[cnt] = i+1
        sol(cnt+1)


sol(0)