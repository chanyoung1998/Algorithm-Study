import sys


def get_lca(a,b,k):
    lca = dict()
    if a == b:
        return a

    for _ in range(1000):
        if a ==- 1:
            break
        lca[a] = True
        a = parent[a]

    while b != -1:
        if b in lca:
            return b
        b = parent[b]



def move_node(a,b):
    parent[a] = b


def paint_node(a,b,c,k):

    lca_a_b = get_lca(a,b,k)

    while a != lca_a_b:
        paint[a] = c
        a = parent[a]

    while b != lca_a_b:
        paint[b] = c
        b = parent[b]


def count_node(a,b,k):

    lca_a_b = get_lca(a, b, k)
    ret = set()
    while a != lca_a_b:
        ret.add(paint[a])
        a = parent[a]

    while b != lca_a_b:
        ret.add(paint[b])
        b = parent[b]

    print(len(ret))



n,m = map(int,sys.stdin.readline().rstrip().split())
parent = [0 for _ in range(n)]
parent[0] = -1

paint =[0 for _ in range(100001)]
for i in range(m):
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    if cmd[0] == 1:
        paint_node(cmd[1],cmd[2],cmd[3],i)
    elif cmd[0] == 2:
        move_node(cmd[1],cmd[2])
    else:
        count_node(cmd[1],cmd[2],i)