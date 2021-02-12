'''
내용:백준 알고리즘 단계별 풀기 그리디 1541 잃어버린 괄호
날짜:21년2월12일
사용 언어:파이썬
'''
#반례 0000-10000+1+0111 이런 형식
expression = list(input())
new_expression = expression.copy()
flag = False
sum_min = 0
temp = 0
count = 0
for i in range(len(expression)):

    if expression[i] == '-' and not flag:
        new_expression.insert(count + i, ')')
        count += 1
        new_expression.insert(count+i+1,'(')
        count += 1
        flag = True
    elif expression[i] == '-' and flag:
        new_expression.insert(count+i,')')
        count += 1
        new_expression.insert(count + i+1, '(')
        count += 1
        flag = False


new_expression.insert(0, '(')
new_expression.append(')')


str_ = ''
for s in new_expression:
    str_ += s
print(eval(str_))







