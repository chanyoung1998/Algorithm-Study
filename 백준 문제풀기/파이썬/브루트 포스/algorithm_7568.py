'''
내용:백준 알고리즘 단계별 풀기 브루트포스 7568 덩치
날짜:21년1월20일
사용 언어:파이썬
'''

# 자신보다 더 큰 덩치의 사람이 k명 이라면 그 사람의 덩치 등수는k+1이 된다.

n = int(input())
hwlist = []
rank = []
for i in range(n):
    hwlist.append(list(map(int,input().split(' '))))

for [h,w] in hwlist:
    count = 0
    for [h_,w_] in hwlist:
        if h_ > h and w_ > w:
            count += 1

    rank.append(count+1)

for k in rank:
    print(str(k)+' ',end='')