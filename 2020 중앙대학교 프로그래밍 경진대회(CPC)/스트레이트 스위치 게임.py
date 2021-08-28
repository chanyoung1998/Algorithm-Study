import sys
import copy
from collections import deque


n, k = map(int,sys.stdin.readline().rstrip().split())
cubes = list(map(int,sys.stdin.readline().rstrip().split()))
switches = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(k)]
init = copy.deepcopy(cubes)
check = set()
def sol():

    queue = deque()
    queue.append((cubes,0))
    check.add(tuple(cubes))
    while queue:
        new_cube,count = queue.popleft()

        if new_cube.count(new_cube[0]) == n:
            print(count)
            return

        for i in range(k):
            increase = i + 1
            temp_cube = copy.deepcopy(new_cube)
            for x in switches[i][1:]:
                temp_cube[x-1] = (temp_cube[x-1]+increase) % 5

            if temp_cube == init:
                continue
            else:
                if tuple(temp_cube) in check:
                    continue
                check.add(tuple(temp_cube))
                queue.append((temp_cube,count+1))
    print(-1)

sol()