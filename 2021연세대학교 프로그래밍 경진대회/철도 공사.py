import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
station = list(map(int,sys.stdin.readline().rstrip().split()))

class SingleNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,node):
        if self.head:

            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = self.head
            self.head.prev = self.tail


        else:
            self.head = node
            self.tail = self.head



    def BN(self,i,j):

        curn = self.head

        if curn.data == i:
            print(curn.next.data)
            newNode = SingleNode(j)
            newNode.next = curn.next
            newNode.prev = curn
            curn.next.prev = newNode
            curn.next = newNode

            return

        curn = curn.next

        while curn != self.head:
            if curn.data == i:
                print(curn.next.data)
                newNode = SingleNode(j)
                newNode.next = curn.next
                newNode.prev = curn
                curn.next.prev = newNode
                curn.next = newNode
                return
            curn = curn.next


        return -1

    def BP(self, i, j):

        curn = self.head

        if curn.data == i:
            targetn = curn.prev
            print(targetn.data)
            newNode = SingleNode(j)
            newNode.next = curn
            newNode.prev = targetn
            curn.prev = newNode
            targetn.next = newNode
            self.tail = newNode
            return

        curn = curn.next

        while curn != self.head:
            if curn.data == i:
                targetn = curn.prev
                print(targetn.data)
                newNode = SingleNode(j)
                newNode.next = curn
                newNode.prev = targetn
                curn.prev = newNode
                targetn.next = newNode

                return

            curn = curn.next


        return -1


    def CN(self,i):

        curn = self.head

        if curn.data == i:
            targetn = curn.next
            print(targetn.data)
            curn.next = targetn.next
            targetn.next.prev = curn

            return


        curn = curn.next

        while curn != self.head:
            if curn.data == i:
                targetn = curn.next
                print(targetn.data)
                curn.next = targetn.next
                targetn.next.prev = curn
                return

            curn = curn.next


        return -1

    def CP(self, i):

        curn = self.head

        if curn.data == i:
            targetn = curn.prev
            print(targetn.data)
            targetn.prev.next = curn
            curn.prev = targetn.prev

            return

        curn = curn.next

        while curn != self.head:
            if curn.data == i:
                targetn = curn.prev
                print(targetn.data)
                targetn.prev.next = curn
                curn.prev = targetn.prev

            curn =curn.next

        return -1




    def print(self):
        curn = self.head
        string = ''

        while curn:
            string += str(curn.data)
            if curn.next:
                string += '->'
            if curn.next == self.head:
                string = '->' + string
                break
            curn = curn.next
        print(string)

circular = CircularLinkedList()
for i in range(len(station)):
    circular.append(SingleNode(station[i]))
    index[station[i]] = i

#circular.print()
for _ in range(m):
    inputs = list(sys.stdin.readline().rstrip().split())
    cmd = inputs[0]
    if cmd == "BN":
        circular.BN(int(inputs[1]),int(inputs[2]))
    elif cmd == 'BP':
        circular.BP(int(inputs[1]),int(inputs[2]))
    elif cmd == "CN":
        circular.CN(int(inputs[1]))
    elif cmd == "CP":
        circular.CP(int(inputs[1]))

    #circular.print()