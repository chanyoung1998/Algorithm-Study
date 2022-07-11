# include <stdio.h>
# include <stdlib.h>
# include <memory.h>
typedef
struct
TreeNode
{
    int
data;
struct
TreeNode * left, *right;
}TreeNode;

/ *
TreeNode
n1 = {1, NULL, NULL};
TreeNode
n2 = {2, & n1, NULL};
TreeNode
n3 = {3, NULL, NULL};
TreeNode
n4 = {4, NULL, NULL};
TreeNode
n5 = {5, & n3, & n4};
TreeNode
n6 = {6, & n2, & n5};
TreeNode * root = & n6;
* /

TreeNode ** n;
TreeNode * make_node(int
item, TreeNode * left, TreeNode * right) {
    TreeNode * new_node = (TreeNode *)
malloc(sizeof(TreeNode));
new_node->data = item;
new_node->left = left;
new_node->right = right;
return new_node;
}
void
inorder(TreeNode * root)
{
if (root) {
inorder(root->left);
printf("%d->", root->data);
inorder(root->right);
}
}

void
preorder(TreeNode * root)
{
if (root) {
printf("%d->", root->data);
preorder(root->left);
preorder(root->right);
}
}

void
postorder(TreeNode * root)
{
if (root) {
postorder(root->left);
postorder(root->right);
printf("%d->", root->data);
}
}

// �������� ����
# define MAX_SIZE 100
int
top = -1;
TreeNode * stack[MAX_SIZE];
void
push(TreeNode * p)
{
if (top < MAX_SIZE - 1) {
stack[++top] = p;
}
}

TreeNode * pop()
{
TreeNode * p = NULL;
if (top >= 0) {
p = stack[top--];
}
return p;
}

void
preorder_iter(TreeNode * root)
{

push(root);
while (top != -1) {
root = pop();
if (!root)
continue;

printf("%d->", root->data);

if (root->right) {
push(root->right);
}
if (root->left) {
push(root->left);
}

}
}

void
preorder_iter2(TreeNode * root)
{

while (1) {
while (root) {
printf("%d->", root->data);
push(root);
root = root->left;
}
root = pop();
if (!root) break;
root = root->right;

}

}

void
inorder_iter(TreeNode * root)
{
while (1) {
while (root) {
push(root);
root = root->left;
}

root = pop();
if (!root) break;

printf("%d->", root->data);
root = root->right;
}
}


void
postorder_iter(TreeNode * root)
{
    TreeNode * stack2[MAX_SIZE];
int
top2 = -1;
push(root);
while (top != -1) {
root = pop();
if (root->left)
push(root->left);
if (root->right)
push(root->right);

stack2[++top2] = root;
}

while (top2 != -1) {
printf("%d->", stack2[top2]->data);
top2 -= 1;
}

}

void
postorder_iter2(TreeNode * root)
{
while (1) {

while (root) {
push(root);
push(root);
root = root->left;
}

if (top != -1) {
root = pop();

if (top != -1 & & root->data == stack[top]->data)
root = root->right;
else {
printf("%d->", root->data);
root = NULL;
}
}
else
    break;

}
}



int
main(void)
{
    n = (TreeNode **)
malloc(sizeof(TreeNode *) * 6);
TreeNode * root;
n[0] = make_node(1, NULL, NULL);
n[1] = make_node(2, n[0], NULL);
n[2] = make_node(3, NULL, NULL);
n[3] = make_node(4, NULL, NULL);
n[4] = make_node(5, n[2], n[3]);
n[5] = make_node(6, n[1], n[4]);
root = n[5];

postorder_iter2(root);

}
