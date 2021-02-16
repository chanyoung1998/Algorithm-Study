'''
내용:백준 알고리즘 단계별 풀기 스택 9012 괄호
날짜:21년2월16일
사용 언어:파이썬
'''
import sys

t = int(input())

for i in range(t):
    ps = list(sys.stdin.readline().rstrip())
    temp = []  # ')'담아놓는 스택
    for parenthesis in ps[::-1]:
        if parenthesis == ')':
            pop_data = ps.pop(-1)
            temp.append(pop_data)
        elif parenthesis == '(':
            if len(temp) == 0:
                break
            else:
                ps.pop(-1)
                temp.pop(-1)

    if ps != [] or len(temp) != 0:
        print('NO')
    else:
        print('YES')



