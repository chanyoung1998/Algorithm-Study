import sys

n,m,k = map(int,sys.stdin.readline().split())
boards = []
for _ in range(n):
    boards.append(list(input()))

for i in range(n):
    for j in range(m):
        if boards[i][j] == 'B':
            boards[i][j] = 1
        else:
            boards[i][j] = 0

# ret = k**2
# for i in range(n-k+1):
#     for j in range(m-k+1):
#         cnt = 0
#         for p in range(k):
#             if p % 2 == 0:
#                 flag = 'B'
#             else:
#                 flag = 'W'
#
#             for q in range(k):
#                 if flag == 'B':
#                     if boards[i+p][j+q] == 'W':
#                         cnt += 1
#                     flag = 'W'
#                 else:
#                     if boards[i+p][j+q] == 'B':
#                         cnt += 1
#
#                     flag = 'B'
#
#         ret = min(ret,cnt, k**2-cnt)
#
# print(ret)




#
# prefixsum = [[0 for _ in range(m)] for _ in range(n)]
#
# for i in range(n):
#     for j in range(m-k+1):
#         cnt = 0
#         flag = 'B'
#         for p in range(k):
#             if flag == 'B':
#                 if boards[i][j + p] == 'W':
#                     cnt += 1
#                 flag = 'W'
#             else:
#                 if boards[i][j + p] == 'B':
#                     cnt += 1
#                 flag = 'B'
#
#         prefixsum[i][j] = cnt
#
# ret = k**2
# for i in range(n-k+1):
#     for j in range(m-k+1):
#         cnt = 0
#         for p in range(k):
#             if p % 2 == 0:
#                 cnt += prefixsum[i+p][j]
#             else:
#                 cnt += k - prefixsum[i+p][j]
#
#         ret = min(ret,cnt,k**2-cnt)
#
# print(ret)


prefixsum = [[0 for _ in range(m)] for _ in range(n)]
predict = [[ (j+i) % 2 for i in range(1,m+1)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if m == 0:
            prefixsum[i][j] = 0 if predict[i][j] == boards[i][j] else 1
        else:
            prefixsum[i][j] = prefixsum[i][j-1] + (0 if predict[i][j] == boards[i][j] else 1)

ret = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(k-1,m):
        ret[i][j] = prefixsum[i][j] - (prefixsum[i][j-k] if j - k >= 0 else 0)


prefixsum2 = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        prefixsum2[i][j] = (prefixsum2[i-1][j] if i-1 >= 0 else 0) + ret[i][j]

ret = k**2
for i in range(k-1,n):
    for j in range(k-1,m):

        cnt = prefixsum2[i][j] - (prefixsum2[i-k][j] if i-k >= 0 else 0)
        ret = min(ret,cnt,k**2-cnt)

print(ret)