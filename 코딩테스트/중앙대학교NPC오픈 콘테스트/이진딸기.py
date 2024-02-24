import sys

t = int(sys.stdin.readline())

def print_strawberry(number):

    binary = []
    while number > 0:
        if number % 2 == 1:
            binary.append(1)
        else:
            binary.append(0)
        number //= 2

    while len(binary) != 4:
        binary.append(0)
    ret = ''
    for i in binary[::-1]:
        if i == 0:
            ret += 'V'
        else:
            ret += '딸기'
    print(ret)
    return


for _ in range(t):
    n = int(sys.stdin.readline())

    group = -1
    if n % 14 == 0:
        group = n // 14 - 1
    else:
        group = n // 14

    count = n - group * 14 - 1
    # 1~14
    if group % 2 == 0:
        array = list(range(1,15))
        print_strawberry(array[count])
    # 15~2
    else:
        array = list(range(15,1,-1))
        print_strawberry(array[count])
