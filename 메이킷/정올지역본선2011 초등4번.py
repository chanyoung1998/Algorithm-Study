import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
height = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    tall,short = map(int,sys.stdin.readline().rstrip().split())
    height[tall][short] = 1

for k in range(1, N+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(1, N+1):
        for j in range(1, N+1):
            if height[i][k] ==1 and height[k][j] == 1:
                height[i][j] = 1 #자신보다 작은 경우

cnt = 0
for i in range(1, N+1):
    known_height = 0
    for j in range(1, N+1):
        known_height += height[i][j] + height[j][i] #자신보다 작은사람과 큰사람의 합
    if known_height == N-1: #자신의 키 순서를 알 경우
        cnt += 1
print(cnt)
