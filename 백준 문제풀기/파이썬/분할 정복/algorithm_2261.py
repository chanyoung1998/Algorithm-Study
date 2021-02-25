'''
내용:백준 알고리즘 단계별 풀기 분할 정복 2261 가장 가까운 두점
날짜:21년2월25일
사용 언어:파이썬
'''
import sys
n = int(sys.stdin.readline())
point = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
point.sort(key= lambda x : x[0])
