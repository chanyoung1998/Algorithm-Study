'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  11054 가장 긴 바이토닉 수열
날짜:21년2월3일
사용 언어:파이썬
'''

n = int(input())
A = list(map(int,input().split()))
dp = [0 for _ in range(1001)]

