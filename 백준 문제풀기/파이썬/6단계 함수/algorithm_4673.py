'''
내용:백준 알고리즘 단계별 풀기 함수 4673 셀프 넘버
날짜:21년1월9일
사용 언어:파이썬
'''

def dn(n:int):
    result  = 0
    str_n = str(n)

    for i in str_n:
        result = result+ int(i)

    result = result +n

    return  result

a = []

for i in range(1,10001):
    k = dn(i)
    a.append(k)

for j in range(1,10001):
    if j in a:
        continue
    else:
        print(j)
