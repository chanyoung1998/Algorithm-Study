import sys

n = int(sys.stdin.readline().rstrip())
liquids = list(map(int,sys.stdin.readline().rstrip().split()))
liquids.sort()

ret = sys.maxsize
ret_cord =[]
for i in range(n-2):
    start = i + 1
    end = n-1

    sum_ = liquids[start]+ liquids[end] + liquids[i]
    while start < end:

        if ret > abs(sum_):
            ret = abs(sum_)
            ret_cord = [i,start,end]

        if sum_ > 0:
            sum_ -= liquids[end]
            end -= 1
            sum_ += liquids[end]
        else:
            sum_ -= liquids[start]
            start += 1
            sum_ += liquids[start]


print(*sorted([liquids[ret_cord[0]],liquids[ret_cord[1]],liquids[ret_cord[2]]]))