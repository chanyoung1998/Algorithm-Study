''' 
내용:백준 알고리즘 재귀단계 2477 별 찍기-10
날짜:21년1월16일 
사용 언어:파이썬

분할정복알고리즘 이용하기

'''


def stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return (list(matrix))


star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)