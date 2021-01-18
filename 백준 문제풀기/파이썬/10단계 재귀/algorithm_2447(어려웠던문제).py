''' 
내용:백준 알고리즘 재귀단계 2477 별 찍기-10
날짜:21년1월16일 ~18일
사용 언어:파이썬

분할정복알고리즘 이용하기

크기 3의 패턴은 가운데에 공백이 있고, '가운데'를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
문제에서 '가운데'를 강조한 데에는 이유가 있었다.!
'''


def stars(star_):
    matrix = []
    for i in range(3*len(star_)):
        if i // len(star_) == 1:
            matrix.append(star_[i%len(star_)] + ' '*len(star_) +star_[i%len(star_)])
        else:
            matrix.append(star_[i%len(star)]*3)

    return matrix


star = ['***',"* *","***"]

input_num = int(input())
e = 0

while input_num != 3:
    input_num = input_num/3
    e += 1

for i in range(e):
    star = stars(star)

for i in star:
    print(i)
