import sys

n = int(sys.stdin.readline())
operations = list(sys.stdin.readline().strip())
ret = -sys.maxsize


def backtracking(index, current, status):
    global ret

    if index == n  + 1:
        ret = max(ret,eval(current))
        return


    if index < n - 1:
        if status == 0:
            backtracking(index + 2, current + "(" + operations[index] + operations[index+1], 1)
            backtracking(index+2, str(eval(current + operations[index])) + operations[index+1], 0)
        else:
            backtracking(index+2,str(eval(current + operations[index] + ")")) + operations[index+1], 0)

    elif index == n - 1:
        if status == 0:
            backtracking(index+2, current + operations[index],status)
        else:
            backtracking(index+2, current + operations[index] + ")",status)

backtracking(0,"(",1)
backtracking(0,"",0)

print(ret)