# 출처:https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2
# (이코테 2021 강의 몰아보기)2.그리디 구현 중 모함가 길드 문제 코드
n = int(input())
adventurers = list(map(int,input().split()))
adventurers.sort()
count = 0

for adventurer in adventurers:
