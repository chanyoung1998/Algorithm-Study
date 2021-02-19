from collections import deque

n = int(input())

deq = deque(range(1,n+1))
flag = False
while len(deq) != 1:
    if not flag:
        deq.popleft()
        flag = True
    else:
        pop_data = deq.popleft()
        deq.append(pop_data)
        flag = False

print(deq[0])