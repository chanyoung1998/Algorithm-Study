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
                return 0
            current = current.children[chr]

        return 1

n,m = map(int,sys.stdin.readline().rstrip().split())

trie = Trie()
for _ in range(n):
    trie.insert(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(m):
    cnt += trie.search(sys.stdin.readline().rstrip())

print(cnt)