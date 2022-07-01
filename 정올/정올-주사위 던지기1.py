import sys

n ,m = map(int,sys.stdin.readline().rstrip().split())
ret = [-1 for _ in range(n)]

def func1(cnt):  # 1~6이 적힌 카드가 있을 때 카드를 3장 뽑아 나열하는 경우의 수, 단 각 카드는 충분히 많다
    global n
    if cnt == n:
        print(*ret)
        return
    for i in range(1,7):
        ret[cnt] = i
        func1(cnt+1)

def func2(cnt,idx): # 1~6이 적힌 카드가 있을 때 카드를 3장 뽑는 경우의 수, 단 각 카드는 충분히 많다.
    global n
    if cnt == n:
        print(*ret)
        return
    for i in range(idx,7):
        ret[cnt] = i
        func2(cnt+1,i)

visit = [False for _ in range(7)]
def func3(cnt): #1~6명의 사람이 있고 3개의 각기 다른 의자가 있을 때 의자 앉는 경우의 수
    global n
    if cnt == n:
        print(*ret)
        return
    for i in range(1,7):
        if not visit[i]:
            ret[cnt] = i
            visit[i] = True
            func3(cnt+1)
            visit[i] = False



if m == 1:
    func1(0)
elif m==2:
    func2(0,1)
elif m==3:
    func3(0)