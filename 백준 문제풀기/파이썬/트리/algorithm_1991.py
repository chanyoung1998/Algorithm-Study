'''
내용:백준 알고리즘 단계별 풀기 동적계획과 트리 1991 트리의 순회
날짜:21년4월 22일
사용 언어:파이썬
'''
import sys


n = int(sys.stdin.readline())
node = [[-1,-1] for _ in range(n+1)]
for _ in range(n):
    temp = list(map(ord,sys.stdin.readline().rstrip().split()))
    number = temp[0] - 65
    left = temp[1] - 65
    right = temp[2] - 65
    if left >= 0:
        node[number][0] = left
    if right >= 0:
        node[number][1] = right

def pretravel(num):

    if num == -1:
        return

    print(chr(num+65),end='')
    pretravel(node[num][0])
    pretravel(node[num][1])

def intravel(num):

    if num == -1:
        return

    intravel(node[num][0])
    print(chr(num+65),end='')
    intravel(node[num][1])

def posttravel(num):

    if num == -1:
        return

    posttravel(node[num][0])
    posttravel(node[num][1])
    print(chr(num+65),end='')
pretravel(0)
print()
intravel(0)
print()
posttravel(0)


