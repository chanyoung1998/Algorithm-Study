# 출처:https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2
# (이코테 2021 강의 몰아보기)2.그리디 구현 중 모함가 길드 문제 코드
n = int(input())
adventurers = list(map(int,input().split()))
adventurers.sort()
count = 0 #현재 만들어 지고 있는 그룹에 포험된 모험가의 수
group = 0 #그룹의 수
for adventurer in adventurers:
    count += 1
    if count >= adventurer:
        group += 1
        count = 0
print(group)
