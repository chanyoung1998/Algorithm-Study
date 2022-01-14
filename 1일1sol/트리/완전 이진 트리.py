import sys

k = int(sys.stdin.readline())
input_array = list(map(int,sys.stdin.readline().rstrip().split()))
level = [[] for _ in range(k+1)]
def func(lev,start,end):
    if start == end:
        level[lev].append(input_array[start])
        return
    mid = (start+end) // 2
    level[lev].append(input_array[mid])
    func(lev+1,start,mid-1)
    func(lev+1,mid+1,end)

func(1,0,2**k-2)
for ret in level[1:]:
    print(*ret)


