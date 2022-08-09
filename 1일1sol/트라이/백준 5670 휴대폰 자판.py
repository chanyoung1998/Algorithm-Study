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
        current = self.head.children[string[0]]
        cnt = 1
        for chr in string[1:]:
            if (len(current.children) + (current.data != None)) != 1:
                cnt += 1
            current = current.children[chr]


        return cnt

while True:
    n = sys.stdin.readline()
    if n:
        n = int(n)
        trie = Trie()
        words = [sys.stdin.readline().rstrip() for _ in range(n)]
        ret = 0
        for word in words:
            trie.insert(word)

        for word in words:
            ret += int(trie.search(word))
        print(f'{ret/n:.2f}')
    else:
        break
