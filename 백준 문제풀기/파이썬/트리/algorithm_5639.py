'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 5639 이진 검색 트리
날짜:21년4월 24일
사용 언어:파이썬
'''

import sys
sys.setrecursionlimit()

preorder = [50,30,24,5,28,45,98,52,60]

'''count = 0
while count <= 10000:
    try:
        num = int(input())
    except:break
    preorder.append(num)
    count += 1
'''


def sol(start,end):
    if start == -1 and end == -1:
        return

    root = start
    left_tree_start = -1
    left_tree_end = -1
    right_tree_start = -1
    right_tree_end = -1

    if start == end:
       pass
    elif preorder[root] < preorder[root + 1]:
        # left트리 없을 경우
        right_tree_start = root + 1
        right_tree_end = end
    elif preorder[root] > preorder[root + 1]:
        # left트리 있을 경우
        left_tree_start = root + 1
        flag = False
        for i in range(start,end+1):
            if preorder[i] > preorder[root]:
                left_tree_end = i-1
                right_tree_start = i
                right_tree_end = end
                flag = True
                break
        if not flag:
            left_tree_end = end
    sol(left_tree_start,left_tree_end)
    sol(right_tree_start,right_tree_end)
    print(preorder[root])
    return


sol(0,len(preorder)-1)

