'''
내용:백준 알고리즘 단계별 풀기 큐 11866 요세푸스 문제0
날짜:21년2월18일
사용 언어:파이썬
'''


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

'''
from collections import deque
n, k = map(int, input().split())
numbers = deque(i for i in range(1, n + 1))

print('<', end='')
while numbers:
    for i in range(k - 1):
        numbers.append(numbers[0])
        numbers.popleft()
    print(numbers.popleft(), end='')

    if numbers:
        print(',', end=' ')
print('>')
'''




