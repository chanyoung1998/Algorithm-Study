'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 2263 트리의 순회
날짜:21년4월 24일
사용 언어:파이썬
'''

import sys
sys.setrecursionlimit(100001)
n = int(sys.stdin.readline().rstrip())
inorder = list(map(int,sys.stdin.readline().rstrip().split()))
postorder = list(map(int,sys.stdin.readline().rstrip().split()))

def make_preorder(in_start,in_end,post_start,post_end):
    if post_start > post_end or in_start > in_end:
        return
    root = postorder[post_end]
    print(root,end=' ')

    index = inorder.index(root)
    make_preorder(in_start,index-1,post_start,post_start+(index-1 - in_start))
    make_preorder(index+1,in_end,post_start+(index-1 - in_start) + 1,post_end-1)

make_preorder(0,len(inorder)-1,0,len(postorder)-1)