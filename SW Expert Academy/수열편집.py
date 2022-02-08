def func(x):
    if x % 2 == 0:
        return x // 2 - 1
    else:
        return x//2

for t in range(int(input())):
    n = int(input())
    inputs = [list(map(func,list(map(int,input().rstrip().split())))) for _ in range(n)]
    for i in range(n):
        if inputs[i][0] > inputs[i][1]:
            inputs[i][0],inputs[i][1] = inputs[i][1],inputs[i][0]
    inputs.sort(key=lambda x:(x[0]))
    cnt = 0
    visit = [False for _ in range(n)]
    sum_visit = 0
    while sum_visit != n:
        start = -1
        end = -1
        # 한번에 겹치지 않고 최대한 많이 보내기
        for i in range(n):
            if not visit[i]:
                if inputs[i][0] > end:
                    end = inputs[i][1]
                    visit[i] = True
                    sum_visit += 1

        cnt += 1


    print('#{} {}'.format(t+1,cnt))
