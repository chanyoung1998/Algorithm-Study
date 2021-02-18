import sys

t = int(input())

for i in range(t):
    ps = list(sys.stdin.readline().rstrip())
    temp = []

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