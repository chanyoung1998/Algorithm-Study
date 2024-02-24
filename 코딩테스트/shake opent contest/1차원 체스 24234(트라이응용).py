import sys

sys.setrecursionlimit(1000000)
class Node():
    def __init__(self,data=0):
        self.data = data
        self.count = 0
        self.childList = {}

def add2(root,newNode):
    parent = root
    for next in newNode:
        if next not in parent.childList:
            parent.childList[next] = Node(next)

        parent = parent.childList[next]

    parent.count += 1



def add(root,newNode,idx):

    parent = root

    flag = False
    for next in parent.childList:
        if idx < len(newNode) and next.data == newNode[idx].data:
            add(next,newNode,idx+1)
            flag = True



    if not flag:
        while idx < len(newNode):
            parent.childList.append(newNode[idx])
            parent = newNode[idx]
            idx += 1
        # for node in newNode[idx:]:
        #     parent.childList.append(node)
        #     parent = node

    if len(newNode) == idx:
        parent.count += 1

def travel(root):

    parent = root
    count_sum = 0
    count_squqre = 0

    if parent:
        for next in parent.childList:
            travel(parent.childList[next])
            count_sum += parent.childList[next].count
            count_squqre += (parent.childList[next].count)**2

        parent.count += count_sum
        dp[parent.data] += (count_sum ** 2 - count_squqre) // 2

    return



n,q = map(int,sys.stdin.readline().rstrip().split())
dp = [0 for _ in range(10001)]
root = Node()
for _ in range(n):
    inputs = list(map(int,sys.stdin.readline().rstrip().split()))
    newNode = inputs[1:]
    # for i in range(1,len(inputs)):
    #     newNode.append(inputs[i])
        # newNode.append(Node(inputs[i]))
    # add(root,newNode,0)
    add2(root,newNode)
travel(root)

# print(root)

for _ in range(q):
    print(dp[int(sys.stdin.readline().rstrip())])