package datastructure;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.OptionalInt;

public class BTree2 {


    private int T;
    private Node root;
    private Node newNode;
    private OptionalInt val;


    public BTree2(int t) {
        T = t;
        root = new Node();
        root.leaf = true;
        newNode = null;
        val = OptionalInt.empty();
    }


    class Node{
        List<Integer> key = new ArrayList<>(); // KEY는  최대 2*T-1개
        List<Node> children = new ArrayList<>(); // 자식은 최대 2*T개
        boolean leaf = true; // 해당 노드가 leaf 노드인지 아닌지

        public int find(int target) {
            for (int i = 0; i < key.size(); i++) {
                if (target == key.get(i)) {
                    return i;
                }
            }

            return -1;
        }

    }


    public void insert(int key) {

        newNode = null;
        val = OptionalInt.empty();

        _insert(key, root);

        if (newNode != null) {
            Node newRoot = new Node();
            newRoot.leaf = false;

            newRoot.key.add(val.getAsInt());
            newRoot.children.add(root);
            newRoot.children.add(newNode);

            root = newRoot;
        }
    }

    public void _insert(int key, Node curNode) {

        if (curNode.leaf == true) {
            int pos = lowerBound(curNode.key, key);
            curNode.key.add(pos, key);

            if (curNode.key.size() == 2 * T) {
                newNode = new Node();
                newNode.leaf = true;

                val = OptionalInt.of(curNode.key.get(T)); // 승급할 key

                for (int i = T + 1; i < 2 * T; i++) {
                    newNode.key.add(curNode.key.get(i));
                }

                curNode.key = curNode.key.subList(0, T);
            }

        }
        else{
            int i = 0;
            while (i < curNode.key.size() && key > curNode.key.get(i)) {
                i++;
            }

            _insert(key, curNode.children.get(i));

            if (newNode == null) {  // 더이상 split 필요 x
                return;
            }

            if (curNode.key.size() < 2 * T - 1) {
                curNode.key.add(i, val.getAsInt());
                curNode.children.add(i+1,newNode);
                newNode = null;
            }else{
                curNode.key.add(i, val.getAsInt());
                curNode.children.add(i + 1, newNode);

                split(curNode);
            }

        }

    }

    private void split(Node curNode) {
        newNode = new Node();
        newNode.leaf = false;

        val = OptionalInt.of(curNode.key.get(T));
        for (int i = T + 1; i < 2 * T; i++) {
            newNode.key.add(curNode.key.get(i));
        }
        curNode.key = curNode.key.subList(0, T);

        for (int i = T+1; i <= 2 * T; i++) {
            newNode.children.add(curNode.children.get(i));
        }

        curNode.children = curNode.children.subList(0, T + 1);

    }

    private static int lowerBound(List<Integer> data ,int target) {
        int begin = 0;
        int end = data.size();

        while(begin < end) {
            int mid = (begin + end) / 2;

            if(data.get(mid) >= target) {
                end = mid;
            }
            else {
                begin = mid + 1;
            }
        }
        return end;
    }


    public void Remove(int key) {
        Node x = Search(root, key);

        if (x == null) {
            throw new RuntimeException("해당 키가 존재하지 않습니다.");
        }

        _Remove(root, key,null);

    }

    private void _Remove(Node x, int target,Node parent) {

        int pos = x.find(target);
        if (pos != -1) {
            int i = 0;
            for (; i < x.key.size() && x.key.get(i) != target; i++) {
            }
            if (x.leaf) {
                x.key.remove(i);
                rearrange(x, target, parent);

            }
            else{
                int succ = getSuccessor(target,x.children.get(i+1));
                x.key.add(i, succ);
                x.key.remove(target);

                _Remove(x.children.get(i+1),succ,x);
                rearrange(x,succ,parent);
            }

        }
        else{
            int i = 0;
            for (; i < x.key.size() &&   x.key.get(i) < target ; i++) {
            }
            _Remove(x.children.get(i),target,x);
        }


    }

    private void rearrange(Node x, int target, Node parent) {
        if (x.key.size() < T) {
            //재정렬 필요
            if (x == root) {
                return;
            }
            else{

                int j = 0;
                for (; j < parent.key.size() && parent.key.get(j) < target; j++) {
                }

                //동생 지원
                if (j >= 1 && parent.children.get(j-1).key.size() >= T) {
                    x.key.add(parent.key.remove(j-1));
                    int lastIndex = parent.children.get(j - 1).key.size() - 1;
                    parent.key.add(j-1, parent.children.get(j - 1).key.remove(lastIndex));
                }
                //형 지원
                else if (j < parent.children.size()-1  && parent.children.get(j+1).key.size() >= T) {
                    x.key.add(parent.key.remove(j+1));
                    int firstIndex = 0;
                    parent.key.add(j, parent.children.get(j + 1).key.remove(firstIndex));
                }
                //둘 다 불가능
                else{
//                            if (j == 0) {
//                                parent.children.get(1).key.add(parent.key.remove(0));
//                                for (Integer left : x.key) {
//                                    parent.children.get(j - 1).key.add(left);
//                                }
//                                parent.children.remove(j);
//                            }
                    parent.children.get(j - 1).key.add(parent.key.remove(j - 1));
                    for (Integer left : x.key) {
                        parent.children.get(j - 1).key.add(left);
                    }
                    parent.children.remove(j);
                }
            }

        }
    }

    private int getSuccessor(int target,Node x) {

        while (!x.leaf) {
            x = x.children.get(0);
        }

        return x.key.get(0);


    }

    private Node Search(Node x, int target) {

        int i = 0;
        if (x == null) {
            return x;
        }
        for (i = 0 ; i < x.key.size();i++) {

            if (target < x.key.get(i)) {
                break;
            }

            if (target == x.key.get(i)) {
                return x;
            }
        }

        if(x.leaf){
            return null;
        }else{
            return Search(x.children.get(i), target);
        }




    }

    void traverse() {
        _traverse(root,0);
    }

    void _traverse(Node node,int tab)
    {
        int i;
        String s = "";

        // Print 'tab' number of tabs
        for (int j = 0; j < tab; j++) {
            s += "\t";
        }
        for (i = 0; i < node.key.size(); i++) {

            // If this is not leaf, then before printing key[i]
            // traverse the subtree rooted with child C[i]
            if (node.leaf == false)
                _traverse(node.children.get(i),tab + 1);

            System.out.println(s + node.key.get(i));

        }

        // Print the subtree rooted with last child
        if (node.leaf == false) {
            _traverse(node.children.get(i),tab + 1);
        }
    }
    public static void main(String[] args) {
        BTree2 bTree = new BTree2(3);



        bTree.insert(1);
        bTree.insert(2);
        bTree.traverse();

        bTree.insert(5);
        bTree.insert(6);
        bTree.traverse();

        bTree.insert(3);
        bTree.insert(4);
        bTree.traverse();






  /*      bTree.insert(1);
        bTree.insert(15);
        bTree.insert(2);
        bTree.insert(5);
        bTree.insert(30);
        bTree.insert(90);
        bTree.insert(20);
        bTree.insert(7);
        bTree.insert(9);
        bTree.insert(8);
        bTree.insert(10);
        bTree.insert(50);
        bTree.insert(70);
        bTree.insert(60);
        bTree.insert(40);*/


    }
}
