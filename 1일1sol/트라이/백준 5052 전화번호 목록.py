import sys

class Node():
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self,string):

        current = self.head

        for chr in string:
            if chr not in current.children:
                current.children[chr] = Node(chr)
            current = current.children[chr]

        current.data = string

    def search(self,string):
        current = self.head

        for chr in string:
            if chr not in current.children:
                return False
            current = current.children[chr]

        if current.data!= None:
            return True
        else:
            return False

    def check_consistency(self,string):
        current = self.head

        for chr in string:
            current = current.children[chr]

        if current.children:
            return False
        else:
            return True


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    phone_numbers = [sys.stdin.readline().rstrip() for _ in range(n)]
    tri = Trie()
    for phone in phone_numbers:
        tri.insert(phone)

    for phone in phone_numbers:
        if not tri.check_consistency(phone):
            print("NO")
            break
    else:
        print("YES")



