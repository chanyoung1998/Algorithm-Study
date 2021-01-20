'''
내용:백준 알고리즘 단계별 풀기 브루트포스 2231 분해합
날짜:21년1월20일
사용 언어:파이썬
'''

def dn(n:int):
    result = 0
    str_n = str(n)

    for i in str_n:
        result = result + int(i)

    result = result + n

    return result


n = int(input())
flag = False
for i in range(n):
    if dn(i) == n:
       print(i)
       flag = True
       break

if not flag:
    print(0)





