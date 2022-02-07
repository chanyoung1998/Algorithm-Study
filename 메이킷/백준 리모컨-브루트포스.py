import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
if m:
    not_working = set(sys.stdin.readline().rstrip().split())
else:
    not_working = set()


ret = abs(n-100)

number = n
while number >= 0:
    for num in str(number):
        if num in not_working:
            number -= 1
            break
    else:
        ret = min(ret, len(str(number)) + abs(n - number))
        break

number = n
while number <= 1000001:

    for num in str(number):
        if num in not_working:
            number += 1
            break
    else:
        ret = min(ret, len(str(number)) + abs(n - number))
        break


print(ret)

