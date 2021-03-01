n = int(input())
k = int(input())
s, e = 1, k
ans = 0
while s <= e:
    m = (s + e) // 2
    cnt = 0

    # m보다 이하인 값의 개수 구하기
    for i in range(1, n + 1):
        cnt += min(n, m // i)

    # cnt >= k를 만족하는 m의 값 중 최소의 값을 찾는 것
    if cnt >= k:
        e = m - 1
        ans = m
    else:
        s = m + 1
print(ans)

