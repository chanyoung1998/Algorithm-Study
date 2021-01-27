'''
내용:백준 알고리즘 단계별 풀기 백트래킹 9663 N-Queen
날짜:21년1월27일
사용 언어:파이썬
'''

n = int(input())
cnt = 0
x = [-1 for _ in range(n)]
list_ = []

def NQueen(k):
    if k >= n:
        #print(x)
        list_.append(x)
        return

    for i in range(n):
        if funk(x,k,i): # x[k] = i를 놓을수 있다면
            x[k] = i
            NQueen(k+1)
            x[k] = -1

def funk(x,k,i):
    for j in range(k):
        if x[j] == i or k-j+x[j] == i or x[j]-(k-j) == i:
            return False

    return True

NQueen(0)
print(len(list_))