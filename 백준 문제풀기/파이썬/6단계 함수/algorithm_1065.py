'''
내용:백준 알고리즘 단계별 풀기 함수 1065 한수
날짜:21년1월9일
사용 언어:파이썬
'''


def isHansu(n:int):
    n_str = list(map(int,str(n)))

    if len(n_str) == 1  or len(n_str) == 2:
        return True
    else:
        diff = n_str[1]-n_str[0]

        for i in range(2,len(n_str)):
            p_diff = diff
            diff = n_str[i]-n_str[i-1]
            if p_diff != diff:
                return False

        return True



n = int(input())
count = 0

for i in range(1,n+1):
    if isHansu(i):
        count = count+1
        print(i)
print(count)

