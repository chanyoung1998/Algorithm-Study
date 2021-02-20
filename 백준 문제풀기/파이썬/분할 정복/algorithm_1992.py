'''
내용:백준 알고리즘 단계별 풀기 분할 정복 1992 쿼드 트리
날짜:21년2월20일
사용 언어:파이썬
'''

import sys

def sol(image):
    global ret
    x = len(image)
    sum_bit = 0
    for _ in range(x):
        sum_bit += sum(image[_])

    if sum_bit == x**2:
        ret += '1'
        return
    if sum_bit == 0:
        ret += '0'
        return

    ret += '('
    sol([image[i][:x//2] for i in range(x//2)])
    sol([image[i][x//2:] for i in range(x//2)])
    sol([image[i][:x//2] for i in range(x//2, x)])
    sol([image[i][x//2:] for i in range(x//2, x)])
    ret += ')'


n = int(sys.stdin.readline())
image = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
ret = '('
flag_0 = True
flag_1 = True
for _ in range(n):
    if 0 in image[_]:
        flag_1 = False
    if 1 in image[_]:
        flag_0 = False

if flag_0:
    print(0)

elif flag_1:
    print(1)
else:

    sol([image[i][:n//2] for i in range(n//2)])
    sol([image[i][n//2:] for i in range(n//2)])
    sol([image[i][:n//2] for i in range(n//2, n)])
    sol([image[i][n//2:] for i in range(n//2, n)])

    print(ret + ')')


