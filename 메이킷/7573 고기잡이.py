import sys

n,l,m = map(int,sys.stdin.readline().split())
fishes = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(m)])
fishesY = [fish[1] for fish in fishes]
l//=2

result=0
# 그물 크기 구하기
for w in range(1,l):
    h=l-w

    # i번째 물고기와 같은 그물에 있을 수 있는 물고기 구하기 (x 확인)
    j=0
    for i in range(m):
        while j<m and fishes[j][0]-fishes[i][0]<=h:
            j+=1
        targetFishes = sorted(fishesY[i:j])

        # ii번째 물고기와 같은 그물에 있을 수 있는 물고기 구하기 (y 확인)
        jj=0
        for ii in range(j-i):
            while jj<j-i and targetFishes[jj]-targetFishes[ii]<=w:
                jj+=1
            result = max(result,jj-ii)
print(result)