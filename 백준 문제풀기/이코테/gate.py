import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
gates = [int(sys.stdin.readline()) for _ in range(p)]
# 시간초과 발생
'''dp = [0 for _ in range(g)]
count = 0
for gate in gates:
    i = gate-1
    flag = False
    while i >= 0:
        if dp[i] == 0:
            dp[i] = 1
            count += 1
            flag = True
            break
        i -= 1

    if not flag:
        break

print(count)'''

parent = [i for i in range(g+1)]

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

count = 0
for gate in gates:
    data = find_parent(gate)
    if data == 0:
        break
    union(data,data-1)
    count += 1
print(count)