'''
내용:백준 알고리즘 단계별 풀기 스택 10828 스택
날짜:21년1월20일
사용 언어:파이썬
'''
import sys
class IntStack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self,num):
        self.stack.append(num)
        self.top += 1

    def pop(self):
        if self.top == -1:
            print(-1)
            return
        pop_data = self.stack.pop()
        self.top -= 1
        print(pop_data)
        return pop_data

    def size(self):
        print(len(self.stack))
        return len(self.stack)

    def empty(self):
        if self.top == -1:
            print(1)
            return True
        else:
            print(0)
            return False

    def top_(self):
        if self.top == -1:
            print(-1)
            return
        else:
            print(self.stack[-1])
            return


n = int(sys.stdin.readline().rstrip())
IS = IntStack()
for i in range(n):
    cmd = sys.stdin.readline().rstrip()

    if 'push' in cmd:
        temp = cmd.split()
        IS.push(int(temp[1]))
    elif 'pop' == cmd:
        pop_data = IS.pop()
    elif 'size' == cmd:
        size = IS.size()
    elif 'empty' == cmd:
        empty = IS.empty()
    elif 'top' == cmd:
        IS.top_()








