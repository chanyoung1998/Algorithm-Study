import sys
import re
from functools import cmp_to_key

n = int(sys.stdin.readline())
arr = [] * n
temp = []
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    temp = re.findall("[a-zA-Z]|[0-9]+",string)
    arr.append([string,temp])

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

def comp(a,b):
    for i in range(min(len(a[1]), len(b[1]))):
        if a[1][i].isdigit() and b[1][i].isalpha():
            return -1
        elif a[1][i].isalpha() and b[1][i].isdigit():
            return 1
        elif a[1][i].isdigit() and b[1][i].isdigit():
            if int(a[1][i]) == int(b[1][i]):
                if len(a[1][i]) == len(b[1][i]):
                    continue
                else:
                    return len(a[1][i]) - len(b[1][i])
            else:
                return int(a[1][i]) - int(b[1][i])
        else:
            if a[1][i] == b[1][i]:
                continue
            else:
                return alphabet.index(a[1][i]) - alphabet.index(b[1][i])

    return len(a[1]) - len(b[1])

anwer = sorted(arr,key= cmp_to_key(comp))
for i in anwer:
    print(i[0])