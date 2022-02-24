import sys
MOD = 100003

def mod(n):
    return n % MOD


def check(mid):
    pos = [[] for _ in range(MOD)]
    H = 0
    power = 1
    found = False
    for i in range(0,l-mid+1):
        if i == 0:
            for j in range(0,mid):
                H = mod(H + ord(inputs[mid-1-j]) * power)
                if j < mid- 1:
                    power = mod(power*2)
        else:
            H = mod(2*(H-ord(inputs[i-1]) * power) + ord(inputs[i+mid-1]))

        if pos[H]:
            for p in pos[H]:
                same = True
                for j in range(mid):
                    if inputs[i+j] != inputs[p+j]:
                        same = False
                        break

                if same:
                    return True

        pos[H].append(i)

    return False


l = int(sys.stdin.readline())
inputs = list(sys.stdin.readline().rstrip())
left = 0
right = l

while left + 1 < right:
    mid = (left+right) // 2

    if check(mid):
        left = mid
    else:
        right = mid

print(left)
