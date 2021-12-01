import sys

n = int(sys.stdin.readline())
inputs = list(map(int,sys.stdin.readline().rstrip().split()))
add,minus,mul,div = map(int, sys.stdin.readline().rstrip().split())

max_ret = -sys.maxsize
min_ret = sys.maxsize
def dfs(i,x):

    global max_ret,min_ret,add,minus,mul,div
    if i == n:
        max_ret = max(max_ret,x)
        min_ret = min(min_ret,x)

    if add > 0:
        add -= 1
        dfs(i+1,x + inputs[i])
        add += 1

    if minus > 0:
        minus -= 1
        dfs(i+1,x - inputs[i])
        minus += 1

    if mul > 0:
        mul -= 1
        dfs(i+1,x * inputs[i])
        mul += 1


    if div > 0:
        div -= 1
        dfs(i+1,int(x/inputs[i]))
        div += 1

dfs(1,inputs[0])
print(max_ret)
print(min_ret)