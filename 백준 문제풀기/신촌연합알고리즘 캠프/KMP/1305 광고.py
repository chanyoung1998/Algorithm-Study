import sys

l = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
def computeLps():
    lps = [0] * l
    i = 1
    leng = 0

    while i < l:

        if s[i] == s[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

    return lps

print(l-computeLps()[-1])