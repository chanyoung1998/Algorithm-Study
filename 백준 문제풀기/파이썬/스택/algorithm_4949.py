'''
내용:백준 알고리즘 단계별 풀기 스택 4949 균형잡힌 세상
날짜:21년2월16일
사용 언어:파이썬
'''
import sys
while True:
    string = list(sys.stdin.readline().rstrip())
    ps = []
    ps_temp = []
    if string == ['.']:
        break
    for str in string:
        if str == '(' or str == ')' or str =='[' or str == ']':
            ps.append(str)
    for parenthesis in ps[::-1]:

        if parenthesis == ')':
            ps_temp.append(parenthesis)
            ps.pop(-1)
        elif parenthesis == '(':
            if len(ps_temp) == 0 or ps_temp[-1] != ')':
                break
            else:
                ps_temp.pop(-1)
                ps.pop(-1)
        elif parenthesis == ']':
            ps_temp.append(parenthesis)
            ps.pop(-1)
        elif parenthesis == '[':
            if len(ps_temp) == 0 or ps_temp[-1] != ']':
                break
            else:
                ps_temp.pop(-1)
                ps.pop(-1)

    if ps != [] or len(ps_temp) != 0 :
        print('no')
    else:
        print('yes')


