import sys

inputs = list(sys.stdin.readline().rstrip())
cows = [[] for _ in range(26)]
for i in range(52):
    cows[ord(inputs[i])-ord('A')].append(i)

cows.sort(key=lambda x: (x[0],x[1]))
#print(cows)
count = 0
for i in range(26):
    for j in range(i+1,26):
        if cows[i][0] < cows[j][0] < cows[i][1] < cows[j][1]:
            count += 1
print(count)
