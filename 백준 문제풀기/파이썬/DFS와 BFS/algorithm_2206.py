'''
내용:백준 알고리즘 단계별 풀기 dfs와bfs 2206번 벽 부수고 이동하기
날짜:21년3월 15일
사용 언어:파이썬
'''
# "현재 상태"를 정점으로 표현하여 그래프를 만들고 최단거리를 구하는 문제
import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
maps = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque()


