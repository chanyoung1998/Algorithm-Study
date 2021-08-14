import sys
import heapq

n, m = map(int,sys.stdin.readline().rstrip().split())
operating_time = list(map(int, sys.stdin.readline().rstrip().split()))
min_operating_time = min(operating_time)

#time에 몇 번째 학생이 타는가?
# 이 부분에서 시간 초과 발생
'''def person_on_rides(time):

    if time < min_operating_time:
        return m

    min_heap = []
    count = m

    for number,op_time in enumerate(operating_time):
        heapq.heappush(min_heap,(op_time,number))

    while time > 0:
        temp = []
        op_time, number = heapq.heappop(min_heap)

        if time - op_time < 0:
            break

        temp.append((operating_time[number],number))
        count += 1
        while min_heap:
            op,num = heapq.heappop(min_heap)
            if op == op_time:
                count += 1
                temp.append((operating_time[num],num))
            else:
                temp.append((op-op_time,num))

        for op, num in temp:
            heapq.heappush(min_heap,(op,num))

        time -= op_time

    return count
'''
def person_on_rides(time):
    children = m
    for i in range(m):
        children += time // operating_time[i]

    return children

# 이 binary search는 문제 없음
'''def binary_search(target):
    start = 0
    end = max(operating_time) * n

    while start < end:
        mid = (start+end) // 2

        if person_on_rides(mid) < target:
            start = mid + 1
        else:
            end = mid

    return end'''

def binary_search(target):
    start = 0
    end = 30 * 2000000000
    result = -1
    while start <= end:
        mid = (start+end) // 2

        children = m
        for i in range(m):
            children += mid // operating_time[i]

        if children < target:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

    return result




if n <= m:
    print(n)
else:
    time_taken = binary_search(n)
    counts = person_on_rides(time_taken - 1)
    children = m

    for i in range(m):
        children += (time_taken-1) // operating_time[i]

    for i in range(m):
        if not (time_taken % operating_time[i]):
            children += 1

        if children == n:
            print(i+1)
            break

