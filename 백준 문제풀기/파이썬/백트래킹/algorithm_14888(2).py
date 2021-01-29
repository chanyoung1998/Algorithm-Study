import sys
from itertools import permutations
n = int(input())
array = list(map(int,input().split()))
operator_ = list(map(int,input().split()))
operator = []


for i in range(4):
    op = ''
    if i == 0:
        op = '+'
    elif i == 1:
        op = '-'
    elif i == 2:
        op = '*'
    elif i == 3:
        op = '//'
    for _ in range(operator_[i]):
        operator.append(op)

def sol():
    max_result = -sys.maxsize
    min_result = sys.maxsize

    for ops in set(permutations(operator,n-1)):
        result = array[0]
        for i,oper in enumerate(ops):
            if oper == "+":
                result += array[i + 1]

            elif oper == "-":
                result -= array[i + 1]

            elif oper == "*":
                result *= array[i + 1]

            else:
                if result < 0:
                    result *= -1
                    result //= array[i + 1]
                    result *= -1
                else:
                    result //= array[i + 1]

        min_result = min(min_result,result)
        max_result = max(max_result,result)

    return max_result,min_result

ret = sol()
print(ret[0],ret[1],sep='\n')