'''
내용:백준 알고리즘 단계별 풀기 백트래킹 14888 연산자 끼워 넣기
날짜:21년1월27일
사용 언어:파이썬
'''



def operate(k):
    if k == n-1 and array[n-1] not in ret:
        ret.append(array[n-1])
        return
    # arr[k]와arr[k+1]사이에 들어갈 operator결정하기
    for op,i in zip(operator,range(n-1)):

        temp = array[k+1]
        if op == '//' and array[k] < 0:
            x = -array[k]
            array[k+1] = -eval(str(x) + op + str(array[k+1]))
        else:
            array[k+1] = eval(str(array[k]) + op + str(array[k+1]))
        operator.remove(op)
        operate(k+1)
        operator.insert(i,op)
        array[k+1] = temp



n = int(input())
array = list(map(int,input().split()))
operator_ = list(map(int,input().split()))
operator = []
ret = []

for i in range(4):
    op = ''
    if i == 0:
        op = '+'
    elif i == 1:
        op = '-'
    elif i == 2:
        op = '*'
    elif i == 3:
        op = '//'
    for _ in range(operator_[i]):
        operator.append(op)
#print(operator)

operate(0)
print(max(ret),min(ret),sep = '\n')
