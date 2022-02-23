MOD = 100003
MOD2 = 100007

def mod(n):
    return n % MOD

def mod2(n):
    return n % MOD2

def check(parent, pattern):
    cnt = 0
    len_parent = len(parent)
    len_pattern = len(pattern)
    power = 1
    power2 = 1
    power3 = 1
    myHash = 0
    myHash2 = 0
    myHash3 = 0
    for i in range(0, len_pattern):
        myHash = mod(myHash + ord(pattern[len_pattern - 1 - i]) * power)
        myHash2 = mod2(myHash2 + ord(pattern[len_pattern - 1 - i]) * power2)
        myHash3 = mod2(myHash3 + ord(pattern[len_pattern - 1 - i]) * power3)
        if i < len_pattern - 1:
            power = mod(power * 2)
            power2 = mod2(power2 * 3)
            power3 = mod2(power3 * 5)

    H = 0
    H2 = 0
    H3 = 0
    power = 1
    power2 = 1
    power3 = 1
    for i in range(len_parent - len_pattern + 1):
        if i == 0:
            for j in range(0, len_pattern):
                H = mod(H + ord(parent[len_pattern - 1 - j]) * power)
                H2 = mod2(H2 + ord(parent[len_pattern - 1 - j]) * power2)
                H3 = mod2(H3 + ord(parent[len_pattern - 1 - j]) * power3)
                if j < len_pattern- 1:
                    power = mod(power * 2)
                    power2 = mod2(power2 * 3)
                    power3 = mod2(power3 * 5)
        else:
            H = mod(2 * (H - ord(parent[i - 1]) * power) + ord(parent[i + len_pattern - 1]))
            H2 = mod2(3 * (H2 - ord(parent[i - 1]) * power2) + ord(parent[i + len_pattern - 1]))
            H3 = mod2(5 * (H3 - ord(parent[i - 1]) * power3) + ord(parent[i + len_pattern - 1]))

        if H == myHash and H2 == myHash2 and H3 == myHash3:
            cnt += 1
            # same = True
            # for k in range(i, i + len_pattern):
            #     if parent[k] != pattern[k - i]:
            #         same = False
            #         break
            # if same:
            #     cnt += 1

    return cnt


T = int(input())
for t in range(1, T + 1):
    parent = input().rstrip()
    pattern = input().rstrip()
    print('#{} {}'.format(t, check(parent, pattern)))

