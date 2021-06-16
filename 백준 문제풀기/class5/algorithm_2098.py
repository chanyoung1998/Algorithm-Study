import sys
n = int(sys.stdin.readline())
weight = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
city = 16

def inttobinary(number):

    ret = []
    while number > 0 :
        if number % 2 == 0:
            ret.append(0)
        else:
            ret.append(1)
        number = number //2

    ret = [0 for _ in range(n-len(ret))] + ret[::-1]

    return ret

def binarytoint(binary):
    ret = 0
    x = 1
    for i in binary[::-1]:
        ret += i * x
        x *= 2

    return ret

def visit(visited,city):
    visited_binary = inttobinary(visited)
    visited_binary[city] = 1
    return binarytoint(visited_binary)

dp = [[0 for _ in range(2 **(n-1))] for _ in range(n)]

def solution(current,route):

    if dp[current][route] != 0:
        return dp[current][route]

    if route == (1 << (n-1)) -1:
        if weight[current][0]:
            return weight[current][0]
        else:
            return float('inf')

    min_dist = float('inf')
    for j in range(1,n):
        if not weight[current][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = weight[current][j] + solution(j,route | (1 << (j-1)))
        if min_dist > dist:
            min_dist = dist
        dp[current][route] = min_dist
        return min_dist

print(solution(0,0))