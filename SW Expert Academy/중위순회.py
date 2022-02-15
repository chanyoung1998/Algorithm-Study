def inorder(root):
    if child[root][0] != 0:
        inorder(child[root][0])
    print(data[root],end='')
    if child[root][1] != 0:
        inorder(child[root][1])


# T = int(input())
for t in range(1, 10 + 1):
    n = int(input())
    # inputs = []
    parent = [0 for _ in range(n + 1)]
    data = [0 for _ in range(n + 1)]
    child = [[0, 0] for _ in range(n + 1)]
    for _ in range(n):
        inputs = input().rstrip().split()

        p = int(inputs[0])
        data[p] = inputs[1]
        if len(inputs) >= 3:
            if inputs[2] != '_':
                child[p][0] = int(inputs[2])
                parent[int(inputs[2])] = p

        if len(inputs) >= 4:
            if inputs[3] != '_':
                child[p][1] = int(inputs[3])
                parent[int(inputs[3])] = p
    print('#{} '.format(t),end='')
    inorder(1)
    print()
