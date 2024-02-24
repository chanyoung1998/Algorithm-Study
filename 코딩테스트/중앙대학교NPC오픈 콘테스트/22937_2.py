from itertools import accumulate


N, M = int(input()), int(input())
schedule = []
calendar = [0] * 50002

for _ in range(M):
    s, e = map(int, input().split())
    schedule.append((s, e))
    calendar[s] += 1
    calendar[e + 1] -= 1

calendar = list(accumulate(accumulate(calendar)))

day = N * 7
d = max(range(50001 - day), key=lambda x: calendar[x + day] - calendar[x])

start, end = d, d + day
ans = 0

for s, e in schedule:
    if e <= start or s > end:
        continue
    tape = 0
    for cut in range(start, end, 7):
        l, r = max(cut + 1, s), min(cut + 7, e)
        if r - l >= 0:
            tape += 1

    ans += tape

print(ans)