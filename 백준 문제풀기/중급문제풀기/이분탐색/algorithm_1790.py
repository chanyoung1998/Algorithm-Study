import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
'''
- left를 1, right를 n으로 두고 시작한다. mid까지 나열한 수의 길이를 구하고, k보다 작으면 더 큰 수를 구하고,
k보다 크면 k를 포함하고 있으므로 mid 값을 저장하고 더 작은 수를 구한다. 그럼 누적해서 나열한 길이가 k보다 같거나 큰 수의 끝인 ans를 구할 수 있다.
'''
def calc(num):
    exp = 0
    count = 0
    while True:
        if num <= 10 ** (exp + 1) - 1:
            count += (num - 10**exp + 1) * (exp + 1)
            break

        count += (10 ** (exp + 1) - 10 ** exp) * (exp + 1)
        exp += 1

    return count

def binarysearch(n,k):
    left = 1
    right = n
    answer = -1
    while left <= right:

        mid = (left + right) // 2
        len = calc(mid)

        if len < k:
            answer = mid
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer

cnt = binarysearch(n, k)
print(cnt)
length = calc(cnt)
ans = str(cnt)

if calc(n) < k:
    print(-1)
else:
    print(ans[len(ans) - length + k - 1])
