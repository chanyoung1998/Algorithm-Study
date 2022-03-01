import sys

n = int(sys.stdin.readline())
skill = [(int(sys.stdin.readline()),i) for i in range(n)]
temp = [0 for _ in range(n)]
max_ranking = [i for i in range(1,n+1)]


def divide(left,right):
    if left < right:
        mid = (left+right) // 2
        divide(left,mid)
        divide(mid+1,right)
        merge(left,mid,right)


def merge(left,mid,right):
    lp = left
    rp = mid + 1
    idx = left

    while lp <= mid and rp <= right:
        if skill[lp][0] >= skill[rp][0]:
            temp[idx] = skill[lp]

            idx += 1
            lp += 1
        else:
            temp[idx] = skill[rp]
            max_ranking[skill[rp][1]] -= mid-lp +1
            idx += 1
            rp += 1

    if rp > right:
        while lp <= mid:
            temp[idx] = skill[lp]

            idx += 1
            lp += 1
    else:
        while rp <= right:
            temp[idx] = skill[rp]

            idx += 1
            rp += 1

    for i in range(left,right+1):
        skill[i] =temp[i]

divide(0,n-1)
for i in max_ranking:
    print(i)
# print(max_ranking)

