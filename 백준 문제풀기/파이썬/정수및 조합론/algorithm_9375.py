'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 9375 패션왕 신해빈
날짜:21년2월14일
사용 언어:파이썬
'''
'''def sol(i):
    global count
    if i == len(clothes.keys()):
        if 1 not in dp:
            return
        temp = 1
        for i,d in enumerate(dp):
            if d == 1:
                temp *= clothes[list(clothes.keys())[i]]

        count += temp
        return
    dp[i] = 1
    sol(i+1)
    dp[i] = 0
    sol(i+1)
'''

t = int(input())
for i in range(t):
    n = int(input())
    clothes = dict()
    count = 1
    for i in range(n):
        temp = input().split()
        if temp[1] not in clothes.keys():
            clothes[temp[1]] = 1
        else:
            clothes[temp[1]] += 1
    for key in clothes.keys():
        count *= clothes.get(key)+1
    print(count-1)

