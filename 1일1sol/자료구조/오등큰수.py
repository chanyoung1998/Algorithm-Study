'''
24 06 16
오등큰수
17299
골3
스택
'''

import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
numbers = list(map(int,sys.stdin.readline().strip().split(' ')))
fdict = defaultdict(int)
ngf = [-1 for _ in range(n)]
for num in numbers:
    fdict[num] += 1

stack = []

for i in range(n-1,-1,-1):

    if not stack:
        stack.append(i)
    else:
        curf = fdict[numbers[i]]
        while stack and fdict[numbers[stack[-1]]] <= curf:
            stack.pop()

        if stack:
            ngf[i] = numbers[stack[-1]]

        stack.append(i)

print(*ngf)
