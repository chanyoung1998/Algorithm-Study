import sys

n = int(sys.stdin.readline())
schedule = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
schedule.sort(key=lambda x:(x[0],-(x[1]-x[0])))
#print(schedule)
max_date = 0
for s,e in schedule:
    max_date = max(max_date,e)

dates = [[0 for _ in range(max_date+1)]]
for s,e in schedule:
    flag = False
    for date in dates:
        if date[s] == 1:
            continue
        for i in range(s,e+1):
            date[i] = 1
        flag = True
        break
    if not flag:
        dates.append([0 for _ in range(max_date+1)])
        for i in range(s,e+1):
            dates[-1][i] = 1

'''for _ in dates:
    print(_)
'''
max_width = 0
max_len = 0
ret = 0
for i in range(max_date+1):
    count = 0
    for date in dates:
        if date[i] == 0:
            count += 1

    if count == len(dates):
        ret += max_width * max_len
        max_width = 0
        max_len = 0
    else:
        max_width = max(max_width,len(dates)-count)
        max_len += 1
print(ret + max_width * max_len)

'''
import sys
input = sys.stdin.readline

n = int(input())
schedule = [0 for _ in range(367)]

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        schedule[i] += 1

ans = 0
width = 0
height = 0
for i in range(1, 367):
    if schedule[i] > 0:
        width += 1
        height = max(height, schedule[i])
    else:
        ans += width * height
        width = 0
        height = 0

print(ans)
'''