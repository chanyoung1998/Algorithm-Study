# https://herong.tistory.com/entry/SWEA-3813-%EA%B7%B8%EB%9E%98%EB%8F%84-%EC%88%98%EB%AA%85%EC%9D%B4-%EC%A0%88%EB%B0%98%EC%9D%B4-%EB%90%98%EC%96%B4%EC%84%9C%EB%8A%94
# 일반 문제를 결정문제로 바꾸어 생각하여 문제를 풀어야 한다.
# 거꾸로 생각하는 것으로
# 답을 X라고 가정했을때 X가 답인 경우엔 X보다 큰 값은 모두 답이고, X가 답이 아닌 경우는 X보다 작은 값은 모두 답이 될 수 없다.
def check(mid):

    j = 0
    ret = 0
    for i in range(k):

        while j < n:
            if j + block[i]-1 >= n:
                break
            for w in range(j,j+block[i]):
                if wear_level[w] > mid:
                    j = w+1
                    break
            else:
                ret += 1
                j = j + block[i]
                break

    return ret == k



T = int(input())
for t in range(T):
    n,k = map(int,input().rstrip().split())
    wear_level = list(map(int,input().rstrip().split()))
    block = list(map(int,input().rstrip().split()))

    start = 0
    end = 200000
    while start + 1 < end:
        mid = (start + end) // 2

        if check(mid):
            end = mid
        else:
            start = mid

    print('#{} {}'.format(t+1,end))