import sys

inputs = list(sys.stdin.readline().rstrip())

def check(parentesis):
    stack = []

    for prts in parentesis:
        if prts == '[' or prts =='(':
            stack.append(prts)
        else:
            if prts ==')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            elif prts == ']':
                if stack:
                    if stack[-1] =='[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
    if stack:
        return False
    else:
        return True

def calculate(parentesis):
    stack = []
    plusstack = []
    for prts in parentesis:
        if prts =='[' or prts =='(':
            stack.append(prts)
        else:
            if prts == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(2)
                else:
                    plus = 0
                    while stack[-1] != '(':
                        plus += stack[-1]
                        stack.pop()
                    stack.pop()
                    stack.append(plus * 2)

            elif prts ==']':
                if stack[-1] == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    plus = 0
                    while stack[-1] !='[':
                        plus += stack[-1]
                        stack.pop()
                    stack.pop()
                    stack.append(plus*3)

    ret = 0
    while stack:
        ret += stack.pop()

    return ret







if check(inputs):
    print(calculate(inputs))
else:
    print(0)