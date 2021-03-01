'''
내용:백준 알고리즘 단계별 풀기 이분탐색 1300 K번째 수
날짜:21년2월28일
사용 언어:파이썬
'''

# 이 방법으로 해보면 예를들어 n = 5일 때
# 1 2 2 3 3 4 4 4 5 5 6 6 8 8 9 10 10 12 12 15 15 16 20 20 25
# 다 잘 나오는데 K = 20,23 등 12 12 15 15 같이 12와 15가 너무 띄엄 띄엄 있어서 오류 발생


#N이하인  값 구하기
def lower_bound(array, n):
    count = 0

    for arr in array:
        if arr[-1] < n:
            count += len(arr)
            continue
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid] >= n:
                end = mid
            else:
                start = mid + 1
        count += end

    return count + 1


n = int(input())
k = int(input())
array = [[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]

start = 1
end = array[n - 1][n - 1]
flag = False
while start <= end:
    mid = (start + end) // 2
    # mid값이 처음으로 나타나타나는 위치
    count = lower_bound(array, mid)

    if count == k:
        flag = True
        break
    elif count > k:
        end = mid - 1
    else:
        start = mid + 1

if flag:
    if k == n*n:
        print(n*n)
    else:
        print(start,mid,end,'flag = True')
else:
    print(end)



