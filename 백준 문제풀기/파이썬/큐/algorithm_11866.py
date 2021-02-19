from collections import deque
n, k =map(int, input().split())
deq = deque(range(1,n+1))
ret = []
temp = 0
while len(ret) != n:
    point = temp
    del_data = []
    for i in deq:
        point += 1
        if point == k:
            ret.append(i)
            del_data.append(i)
            point = 0
    for i in del_data:
        deq.remove(i)
    temp = point

ret_str = '<'
for i,data in enumerate(ret):
    if i == n-1:
        ret_str += str(data)+'>'
    else:
        ret_str += str(data)+', '

print(ret_str)