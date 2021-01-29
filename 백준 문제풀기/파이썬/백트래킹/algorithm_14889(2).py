import sys

input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += a[i][j]
                elif not select[i] and not select[j]:
                    link += a[i][j]
        print(select)
        ans = min(ans, abs(start - link))

# range를 그냥 range(n)이라고 하면 중복된 경우까지 다 계산해 버린다
# 그럼 시간 초과뜰 수도 있음 하지만 range(idx,n)이라고 함으로써 중복된
# 조합들을 스킵할 수 있다!
    for i in range(idx,n):
        if select[i]:
            continue
        select[i] = 1
        dfs(i + 1, cnt + 1)
        select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

select = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)