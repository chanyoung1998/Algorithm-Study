import sys

n = int(sys.stdin.readline().rstrip())
meetings = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

meetings.sort(key=lambda x:(x[2]))

ret = [meetings[0][0]]

e = meetings[0][2]
for index,start,end in meetings[1:]:
    if start >= e:
        ret.append(index)
        e = end
# print(meetings)
print(*ret)