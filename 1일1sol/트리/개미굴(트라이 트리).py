import sys

class Node():
    def __init__(self,data=None):
        self.data = data
        self.nextList = []

def add(root,newNode,idx):

    parent = root

    flag = False
    for next in parent.nextList:
        if next.data == newNode[idx].data:
            add(next,newNode,idx+1)
            flag = True

    if not flag:
        for node in newNode[idx:]:
            parent.nextList.append(node)
            parent = node


def dfs(root,level):

    parent = root
    for next in parent.nextList:
        print('-'*level + next.data)
        dfs(next,level+2)


n = int(sys.stdin.readline().rstrip())
inputs = [list((sys.stdin.readline().rstrip().split())[1:]) for _ in range(n)]
inputs.sort()
root = Node()

for k in range(n):

    newNode = []

    for i in range(len(inputs[k])):
        newNode.append(Node(inputs[k][i]))

    add(root,newNode,0)

# print(root)
dfs(root,0)




