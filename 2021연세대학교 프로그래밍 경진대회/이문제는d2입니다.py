import sys

inputs = sys.stdin.readline().rstrip()
result1 = inputs.find("d2")

if result1 == -1:
    result2 = inputs.find("D2")
    if result2 == -1:
        print("unrated")
    else:
        print("D2")
else:
    print("D2")