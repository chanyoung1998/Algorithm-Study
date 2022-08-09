# 접두사! or 접미사

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

tri = Trie()
tri.insert("abc")
tri.insert("ac")
tri.insert("car")
print(tri.search("ac"))
print(tri.search("ab"))
print(tri.search("car"))
print(tri.search("ca"))
