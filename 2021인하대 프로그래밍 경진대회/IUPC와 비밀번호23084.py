import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
t = [sys.stdin.readline().rstrip() for _ in range(n)]
alphabet_s = [0 for _ in range(26)]
for alpha in s:
    alphabet_s[ord(alpha) - 97] += 1


def sol(test):
    alphabet_test = [0 for _ in range(26)]
    if len(test) < len(s):
        return False
    elif len(test) == len(s):
        for alpha in test:
            alphabet_test[ord(alpha) - 97] += 1
        count = 0
        for i in range(26):
            if alphabet_s[i] != alphabet_test[i]:
                count += abs(alphabet_s[i] - alphabet_test[i])

        if count == 2:
            return True
        else:
            return False
    else:
        for i in range(len(test)):
            alphabet_test[ord(test[i]) - 97] += 1
            if i >= len(s):
                alphabet_test[ord(test[i-len(s)]) - 97] -= 1

            if i >= len(s) - 1:
                count = 0
                for i in range(26):
                    if alphabet_s[i] != alphabet_test[i]:
                        count += abs(alphabet_s[i] - alphabet_test[i])

                if count == 0 or count == 2:
                    return True

        return False




for test in t:
    if sol(test):
        print('YES')
    else:
        print('NO')