import sys

n,k = map(int,sys.stdin.readline().rstrip().split())
arrays = list(map(int,sys.stdin.readline().rstrip().split()))

s = [0 for _ in range(n)]
dic = dict()
dic[0] = 0
sum = 0
for i in range(n):
    sum += arrays[i]
    s[i] = sum

cnt = 0
for i in range(n):
    if s[i] == k:
       cnt += 1

    if s[i]-k in dic.keys():
        cnt += dic[s[i]-k]

    if s[i] in dic.keys():
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1
print(cnt)