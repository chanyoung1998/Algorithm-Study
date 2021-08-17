import sys
#!/usr/bin/env Python
# coding=utf-8
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
date = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(m)]
date.sort()


# 주력의 시작 부분 구하기
s = 1
max_area = 0
for i in range(1,50001):
    area = 0
    max_date = i + 7 * n - 1
    for start,end in date:
        if i <= start and end <= max_date:
            area += (end-start)+1
        elif i <= start <= max_date and end >= max_date:
            area += (max_date-start) + 1
        elif i >= start and i <= end <= max_date:
            area += end-i + 1
        elif start <= i and max_date <= end:
            area += max_date-i +1


    if max_area < area:
        max_area = area
        s = i

#자르는 구간 구하기
count = 0
for start,end in date:

    if end < s or start > s + 7*n - 1:
        continue

    week_start = 7*((start-s if start -s > 0 else 1)//7) + s
    week_end = week_start + 6



    while week_end <= s + 7*n - 1:
        count += 1
        if end <= week_end:
            break
        else:
            week_end += 7

print(count)




