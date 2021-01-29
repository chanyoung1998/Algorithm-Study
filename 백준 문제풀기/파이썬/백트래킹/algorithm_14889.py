'''
내용:백준 알고리즘 단계별 풀기 백트래킹 14889 스타트와 링크
날짜:21년1월29일
사용 언어:파이썬
'''
from itertools import combinations

n = int(input())
player = [i for i in range(n)]
#S =[]
S = [[0, 5, 4, 5, 4, 5, 4, 5,],
[4, 0, 5, 1, 2, 3, 4, 5],
[9, 8, 0, 1, 2 ,3, 1, 2],
[9, 9, 9, 0, 9, 9, 9, 9],
[1, 1, 1, 1, 0, 1, 1, 1],
[8, 7, 6, 5, 4, 0, 3, 2,],
[9, 1, 9, 1, 9, 1, 0, 9],
[6, 5, 4, 3, 2, 1, 9, 0]]
'''for i in range(n):
    S.append(list(map(int,input().split(' '))))
'''
def sol():

    diff = 100000
    cb = list(combinations(player, n // 2))
    st = 0
    li = 0
    for k in range(len(cb)//2):
        start = 0
        link = 0
        for i1,i2 in zip(cb[k],cb[len(cb)-k-1]):
            for j1,j2 in zip(cb[k],cb[len(cb)-k-1]):
                start += S[i1][j1]
                link += S[i2][j2]

        if abs(start-link) < diff:
            diff = abs(start-link)
            #print(cb[k],cb[len(cb)-k-1],start,link)

    return diff

print(sol())
