
# 순열로 풀라고 해서 풀었는데 시간 초과 발생
'''import sys
from itertools import permutations

n = int(sys.stdin.readline())
strings = []
for _ in range(n):
    strings.append(list(sys.stdin.readline().rstrip()))

number = list(range(10))
unique = []
for string in strings:
    for char in string:
        if char not in unique:
            unique.append(char)


strings_index = []
for string in strings:
    temp = []
    for char in string:
        temp.append(unique.index(char))
    strings_index.append(temp)
ret = 0
for permutation in permutations(number,len(unique)):
    sum_of_str = 0
    for string_index in strings_index:
        x = 1
        for index in string_index[::-1]:
            sum_of_str += x * permutation[index]
            x *= 10
    ret = max(ret,sum_of_str)
print(ret)'''

# 그리디 방법으로 풀기

word_n = int(input())

# 단어들 리스트 만들기
word_lst = []
for _ in range(word_n) :
    word_lst.append(input())

# 문자들 마다에 곱해야할 수 딕셔너리화 시키기 {'G': 100, 'C': 1010, 'F': 1, 'A': 10000, 'D': 100, 'E': 10, 'B': 1}
alpha_digit_dic = {}

for each_lst in word_lst :
    cnt = 0
    for i in each_lst :

        if i not in alpha_digit_dic :
            alpha_digit_dic[i] = 10 ** (len(each_lst) - cnt - 1)
        elif i in alpha_digit_dic :
            alpha_digit_dic[i] += 10 ** (len(each_lst) - cnt - 1)
        cnt += 1

# 딕셔너리 Key값을 내림차순으로 솔팅하고 9부터 차례대로 곱해주기
digit_lst = sorted(list(alpha_digit_dic.values()), reverse = True)

sum = 0
for i in range(len(digit_lst)) :
    sum += digit_lst[i] * (9 - i)
ans = sum
print(ans)