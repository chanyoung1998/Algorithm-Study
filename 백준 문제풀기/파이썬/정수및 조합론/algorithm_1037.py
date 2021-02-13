'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 1037
날짜:21년2월13일
사용 언어:파이썬
'''
n = int(input())
real_factor = list(map(int,input().split()))
real_factor.sort()
print(real_factor[0]*real_factor[n-1])
