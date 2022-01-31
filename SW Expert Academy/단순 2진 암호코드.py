
import sys

#sys.stdin = open("input.txt", "r")

def bin_to_num(arr):
    ret = 0
    pow = 1
    for i in arr[::-1]:
        ret += pow * i
        pow *= 2
    return ret




numbers = dict()
numbers[bin_to_num([0,0,0,1,1,0,1])] = 0
numbers[bin_to_num([0,0,1,1,0,0,1])] = 1
numbers[bin_to_num([0,0,1,0,0,1,1])] = 2
numbers[bin_to_num([0,1,1,1,1,0,1])] = 3
numbers[bin_to_num([0,1,0,0,0,1,1])] = 4
numbers[bin_to_num([0,1,1,0,0,0,1])] = 5
numbers[bin_to_num([0,1,0,1,1,1,1])] = 6
numbers[bin_to_num([0,1,1,1,0,1,1])] = 7
numbers[bin_to_num([0,1,1,0,1,1,1])] = 8
numbers[bin_to_num([0,0,0,1,0,1,1])] = 9

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int,sys.stdin.readline().rstrip().split())
    arrays = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
    code = []
    decoded = 0
    for arr in arrays:
        first = -1
        last = -1
        for i in range(len(arr)):
            if arr[i] == 1:
                last = i
            if arr[i] == 1 and first == -1:
                first = i

        if first != last:
            code = [0 for _ in range(56-(last-first+1))] + arr[first:last+1]

            break

    right = 0
    ret = 0
    for i in range(0,len(code),7):
        num = numbers[bin_to_num(code[i:i+7])]
        ret += num
        if i % 2 == 0:
            right += num * 3
        else:
            right += num

    if right % 10 == 0:
        print('#',test_case,' ',ret,sep='')
    else:
        print('#',test_case,' ',0,sep='')


