'''
내용:백준 알고리즘 단계별 풀기 정수론 및 조합론 1010 다리 놓기
날짜:21년2월14일
사용 언어:파이썬
'''

t = int(input())
for i in range(t):
    k, n = map(int,input().split())
    ret = 1
    for i,j in enumerate(range(n,n-k,-1)):
        ret = (ret * j // (i+1))
    print(ret)