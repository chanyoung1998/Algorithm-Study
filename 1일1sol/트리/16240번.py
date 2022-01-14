import sys

def find(x):
    if parent[x] == -1 * x or parent[x] > 0:
        return parent[x]

    parent[x] = find(-1 * parent[x])
    return parent[x]

def union(a,b):

    if a == b:
        return
    if a > 0 and b < 0:
        parent[-1 * b] = a
    elif a < 0 and b > 0:
        parent[-1 * a] = b
    else:
        if a > b:
            parent[-1 * b] = parent[-1 * a]
        else:
            parent[-1 * a] = parent[-1 * b]

    return

#f = open("zamjena/zamjena.in.4f","r")
n = int(sys.stdin.readline())
array1 = list(sys.stdin.readline().rstrip().split())
array2 = list(sys.stdin.readline().rstrip().split())

dictionary = dict()
count = -1
for i in range(n):
    if not str.isdigit(array1[i]) and array1[i] not in dictionary.keys():
        dictionary[array1[i]] = count
        count -= 1

    if not str.isdigit(array2[i]) and array2[i] not in dictionary.keys():
        dictionary[array2[i]] = count
        count -= 1


parent = [-i for i in range(len(dictionary) + 1)]

for i in range(n):

    a = str.isdigit(array1[i])
    b = str.isdigit(array2[i])

    if a and b:
        if array1[i] == array2[i]:
            continue
        else:
            print("NE")
            exit(0)

    elif not a and not b:
        x = find(-1 * dictionary[array1[i]])
        y = find(-1 * dictionary[array2[i]])

        if x > 0 and y > 0:
            if x == y:
                continue
            else:
                print("NE")
                exit(0)

        else:
            union(x,y)
    elif a and not b:
        x = find(-1 * dictionary[array2[i]])
        if x > 0:
            if x == int(array1[i]):
                continue
            else:
                print("NE")
                exit(0)
        else:
            parent[-1 * x] = int(array1[i])
    else:
        x = find(-1 * dictionary[array1[i]])
        if x > 0:
            if x == int(array2[i]):
                continue
            else:
                print("NE")
                exit(0)
        else:
            parent[-1 * x] = int(array2[i])

print("DA")






