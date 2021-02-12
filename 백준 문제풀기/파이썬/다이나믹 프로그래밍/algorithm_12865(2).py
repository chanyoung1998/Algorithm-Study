'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍  12865 배낭 채우가
날짜:21년2월9일
사용 언어:파이썬
'''

n,k = map(int,input().split())
arr = [[0,0]]
knap = [[0 for _ in range(n+1)] for _ in range(k+1)]
for i in range(n):
    arr.append(list(map(int,input().split())))


for k in range(1,k+1):
    for i in range(1,n+1):
        temp1 = 0
        temp2 = 0
        if k - arr[i][0] >= 0:
            temp1 = knap[k-arr[i][0]][i-1] + arr[i][1]
        temp2 = knap[k][i-1]
        knap[k][i] = max(temp1,temp2)

print(max(knap[k+1]))
