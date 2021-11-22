import sys

inputs = sys.stdin.readline().rstrip()

def akaraka(str):
    #print(str)
    if len(str) == 1:
        return True

    for i in range(len(str)//2):
        if str[i] == str[len(str)-i-1]:
            continue
        else:
            return False

    if akaraka(str[:len(str)//2]) and akaraka(str[len(str)-len(str)//2:]):
        return True
    else:
        return False

if akaraka(inputs):
    print("AKARAKA")
else:
    print("IPSELENTI")

