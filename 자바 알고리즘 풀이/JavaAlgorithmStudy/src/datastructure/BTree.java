package datastructure;

public class BTree {

    private int T; // 2*T-1차 B tree , T는 자식 수의 하한 값을 의미
    private Node root;

    public BTree(int t) {
        T = t;
        root = new Node();
        root.n = 0;
        root.leaf = true;
    }

    public class Node{
        int n; // 키의 개수가 몇개인지 저장

        int key[] = new int[2 * T - 1]; // KEY는  최대 T-1개, 최소 CEIL(T/2)-1 개를 가진다.
        Node child[] = new Node[2 * T]; // 자식은 최대 T개, 최소 CEIL(T/2)개를 가진다.
        boolean leaf = true; // 해당 노드가 leaf 노드인지 아닌지

        public int find(int k) {
            for (int i = 0; i < this.n; i++) {
                if (this.key[i] == k) {
                    return i;
                }
            }
            return -1;
        }
    }


    /**
     * Search Key
     * @param x : root node
     * @param key : 찾고자 하는 key
     * @return
     */
    public Node search(Node x, int key) {
        int i = 0 ;
        if (x == null) {
            return x;
        }

        for (i = 0; i < x.n; i++) {
            if (key ==  x.key[i]) {
                return x;
            }
            if (key < x.key[i]) {
                break;
            }
        }

        if (x.leaf) {
            return null;
        }else{
            return search(x.child[i], key);
        }

    }


    void insert(int key) {
        if (root.n == 2*T - 1) { // If root is full, split it
            Node newRoot = new Node();
            newRoot.leaf = false;
            newRoot.n = 0;
            newRoot.child[0] = root;
            root = newRoot;

            splitChild(root,0, root.child[0]);
            insertNonFull(key, root);
        } else {
            insertNonFull(key, root);
        }
    }

    private void insertNonFull(int k, Node x) {
        if (x.leaf) {
            int i = 0;
            for (i = x.n - 1; i >= 0 && k < x.key[i]; i--) {
                x.key[i + 1] = x.key[i];
            }
            x.key[i + 1] = k;
            x.n = x.n + 1;
        } else {
            int i = 0;
            for (i = x.n - 1; i >= 0 && k < x.key[i]; i--) {
            }
            ;
            i++;
            Node tmp = x.child[i];
            if (tmp.n == 2 * T - 1) {
                splitChild(x, i, tmp);
                if (k > x.key[i]) {
                    i++;
                }
            }
            insertNonFull(k,x.child[i]);
        }

    }

    private void splitChild(Node x,int pos, Node node) {

        Node newNode = new Node();
        newNode.leaf = node.leaf;
        newNode.n = T - 1;

        for (int j = 0; j < T - 1; j++) { // Copy upper half of keys to new node
            newNode.key[j] = node.key[j+T];
        }
        if (!node.leaf) { // Copy upper half of child pointers to new node
            for (int j = 0; j < T; j++) {
                newNode.child[j] = node.child[j+T];
            }
        }
        node.n = T - 1; // Shrink original node

        for (int j = x.n; j >= pos+1; j--) { // Make space for new child pointer
            x.child[j+1] = x.child[j];
        }
        x.child[pos+1] = newNode; // Link new child pointer to parent
        for (int j = x.n-1; j >= pos; j--) { // Move keys in parent to make space for new key
            x.key[j+1] = x.key[j];
        }
        x.key[pos] = node.key[T-1]; // Copy middle key to parent
        x.n++;
    }


    public static void main(String[] args) {
        BTree btree = new BTree(3);
        btree.insert(5);
        btree.insert(15);
        btree.insert(3);
        btree.insert(1);
        btree.insert(20);


    }
}




