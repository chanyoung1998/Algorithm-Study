'''
24 03 19
컬러볼
중량제한 1939.py
골2
누적합
'''
import sys
from collections import defaultdict


def getLowerIndex(target, array):
    low = -1
    high = len(array)

    while low + 1 < high:
        mid = (low + high) // 2

        if array[mid] >= target:
            high = mid
        else:
            low = mid

    return low


N = int(sys.stdin.readline().strip())
player = []
# balls = defaultdict(list)
# prefixSum = defaultdict(list)
for _ in range(N):
    color,size = map(int,sys.stdin.readline().strip().split(' '))
    player.append((_,color,size))
    # balls[color].append(size)

# for key in balls.keys():
#     balls[key].sort()
#
#     sum = 0
#     for i in range(len(balls[key])):
#         size = balls[key][i]
#         sum += size
#         prefixSum[key].append(sum)
#
# for i in range(len(player)):
#     color, size = player[i]
#
#     sum = 0
#     for key in balls.keys():
#         if key != color:
#             li = getLowerIndex(size,balls[key])
#             if li != -1:
#                 sum += prefixSum[key][li]
#
#
#     print(sum)
#
#

player.sort(key=lambda x:x[2])
prefixSum = defaultdict(int)
ret = []
# for index,color,size in player:
#     sum = 0
#     for key in prefixSum.keys():
#         if key != color:
#            sum += prefixSum[key]
#
#     prefixSum[color] += size
#
#     ret.append((index,sum))

# ret.sort(key=lambda x : x[0])
# for r in ret:
#     print(r[1])


total = 0
countSize = defaultdict(int)
countColorSize = dict()
for index,color,size in player:



    if size in countColorSize:
        pass
    else:
        countColorSize[size] = defaultdict(int)


    ret.append((index,total-(countSize[size]-countColorSize[size][color])*size-prefixSum[color]))
    # 전체무게 - 같은 크기의 공의 무게(이 때 같은 색깔의 같은 크기의 공의 무게는 제외, 이유는 prefixSum[color]에서 빼주기 때문) - 같은 색깔의 공의 무게

    countSize[size] += 1
    countColorSize[size][color] += 1
    prefixSum[color] += size
    total += size

ret.sort(key=lambda x : x[0])
for r in ret:
    print(r[1])
