'''
내용:백준 알고리즘 단계별 풀기 스택 1874 스택 수열
날짜:21년2월16일
사용 언어:파이썬
'''
import sys
n = int(sys.stdin.readline().rstrip())
stack = []
temp = []
ret = []
ret_string = ''
index = 0

for i in range(n):
    stack.append(int(sys.stdin.readline().rstrip()))

    while stack[index] in temp:
        ret.append(temp.pop(-1))
        ret_string += '-\n'
        index += 1

    temp.append(i+1)
    ret_string += '+\n'

ret_string += '-\n' * len(temp)
ret += temp[::-1]

'''for i in range(1,n+1):
    while stack[index] in temp:
        ret.append(temp.pop(-1))
        ret_string.append('-')
        index += 1
    temp.append(i)
    ret_string.append('+')
'''
'''while len(temp) > 0:
    ret.append(temp.pop(-1))
    ret_string.append('-')
'''
if ret == stack:
    print(ret_string)
else:
    print('NO')
