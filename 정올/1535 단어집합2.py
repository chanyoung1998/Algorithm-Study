import sys


check = set()
ret = []
while True:
    inputs = sys.stdin.readline().rstrip()
    if inputs == 'END':
        break
    inputs = list(inputs.split())
    for str in inputs:
        if str in check:
            continue
        else:
            ret.append(str)
            check.add(str)

    print(*ret)


