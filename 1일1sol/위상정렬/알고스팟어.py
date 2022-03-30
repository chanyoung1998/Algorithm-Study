import sys
from collections import deque
n = int(sys.stdin.readline())

words = [sys.stdin.readline().rstrip() for _ in range(n)]
adjlist = [set() for _ in range(26)]
degree = [0 for _ in range(26)]
#존재하는 알파벳인지 검사하기 위한 배열
alphabet = [0 for _ in range(26)]

for word in words:
    for w in word:
        alphabet[ord(w)-ord('a')] = 1


for i in range(10):
    for j in range(n):
        for k in range(j+1,n):
            if len(words[j]) > len(words[k]): #나중에 나온 문자열이 먼저 나온 문자열의 진-prefix면 반드시 !를 출력해야 함
                flag = True
                for w in range(len(words[k])):
                    if words[j][w] != words[k][w]:
                        flag = False
                        break
                if flag:
                    print("!")
                    exit(0)



            if i < len(words[j]) and i < len(words[k]):
                flag = True
                for w in range(i):
                    if words[j][w] != words[k][w]:
                        flag =False
                        break

                if flag:
                    if words[j][i] == words[k][i]:
                        continue
                    else:
                        index1 = ord(words[j][i]) - ord('a')
                        index2 = ord(words[k][i]) - ord('a')
                        adjlist[index1].add(index2)
for i in range(26):
    if adjlist[i]:
        for next in adjlist[i]:
            degree[next] += 1

q = deque()
for i in range(26):
    if degree[i] == 0 and alphabet[i] == 1:
         q.append(i)


UNIQUE = True
RIGHT = True
ret = ''
while q:
    if len(q) > 1:
        UNIQUE = False
        break
    cur = q.popleft()
    ret += chr(cur+ord('a'))

    for next in adjlist[cur]:
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)



if not UNIQUE:
    print("?")
elif len(ret) != sum(alphabet):
    print("!")
else:
    print(ret)


