'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 1991 트리의 순회
날짜:21년4월 22일
사용 언어:파이썬
'''
import sys

n = int(sys.stdin.readline())
adjlist = [sys.stdin.readline().rstrip().split() for _ in range(n)]
visited = [False for _ in range(n)]
