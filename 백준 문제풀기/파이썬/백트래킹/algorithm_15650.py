'''
내용:백준 알고리즘 단계별 풀기 백트래킹 15650 N과 M(2)
날짜:21년1월26일
사용 언어:파이썬
'''

n,m = map(int,input().split())
x = [0 for _ in range(n)]


def sol(k):
   if k <= n and x.count(1) == m:
       temp = ''
       for i in range(n):
           if x[i] == 1:
               temp += str(i+1) + ' '
       print(temp)
       return

   if k == n:
       return

   x[k] = 1
   sol(k+1)
   x[k] = 0
   sol(k+1)

sol(0)
