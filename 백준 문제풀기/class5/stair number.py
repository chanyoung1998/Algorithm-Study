import sys
#시간 초과 ver
n = int(sys.stdin.readline())
array = [-1 for _ in range(n)]
IsIncluded = [[] for _ in range(10)]
ret = 0
def sol(num,count):
    global ret

    if num == 0 and count == n-1:
        return


    array[count] = num
    IsIncluded[num].append(True)

    if count == n-1:
        flag = True
        for temp in IsIncluded:
            if True not in temp:
                flag = False
                break
        if flag:
            print(*array)
            ret += 1
    else:
        if num == 0:
            sol(1,count+1)

        elif num == 9:
            sol(8,count+1)
        else:
            sol(num+1,count+1)
            sol(num-1,count+1)

    array[count] = -1
    IsIncluded[num].pop()
    return


for i in range(10):
    sol(i,0)
print(ret % 1000000000)