class HuffNode:
    def __init__ (self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def preorder(self):
        print(self.freq, end=" ")

        if (self.left is not None):
            self.left.preorder()
        if (self.right is not None):
            self.right.preorder()

    def inorder(self):
        if (self.left is not None):
            self.left.inorder()

        print(self.freq, end=" ")
        if (self.right is not None):
            self.right.inorder()

def huffman(n, PQ):
    for _ in range(n - 1):
        p = PQ.get()[1]

        q = PQ.get()[1]
        r = HuffNode(' ', p.freq + q.freq)
        r.left = p
        r.right = q
        PQ.put((r.freq, r))
    return PQ.get()[1]

codes = ['a','e','c','a','d','f']
freqs = [405, 10, 12, 16, 17, 25]
from queue import PriorityQueue
PQ = PriorityQueue()
for i in range(len(codes)):
    node = HuffNode(codes[i], freqs[i])
    PQ.put((node.freq, node))

root = huffman(len(codes), PQ)
print("Preorder:", end=" ")
root.preorder()
print("\nInorder:", end=" ")
root.inorder()
print()

huff_dict = {}
def mapping_Bit(node,string):

    if node.left:
        mapping_Bit(node.left,string+'0')
    elif node.right:
        mapping_Bit(node.right,string+'1')
    else:
        huff_dict[node.symbol] = string

    return

mapping_Bit(root,'')

print(huff_dict)

