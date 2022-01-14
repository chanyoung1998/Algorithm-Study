import sys

keys = list(sys.stdin.readline().rstrip())
codes = list(sys.stdin.readline().rstrip())
alphabet = [0 for _ in range(26)]
for i in range(len(keys)):
    alphabet[i] = keys[i]
#print(alphabet)
for code in codes:
    if code == ' ':
        print(' ',end='')
        continue

    if code.isupper():
        code = code.lower()
        print(alphabet[ord(code)-97].upper(),end='')
    else:
        print(alphabet[ord(code)-97],end='')