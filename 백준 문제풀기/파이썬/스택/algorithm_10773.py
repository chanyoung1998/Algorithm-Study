'''
내용:백준 알고리즘 단계별 풀기 스택 10773
날짜:21년2월16일
사용 언어:파이썬
'''
import sys

k = int(sys.stdin.readline().rstrip())
stack = []
for i in range(k):
    temp = int(sys.stdin.readline())
    if temp != 0:
        stack.append(temp)
    elif temp == 0:
        stack.pop(-1)

print(sum(stack))