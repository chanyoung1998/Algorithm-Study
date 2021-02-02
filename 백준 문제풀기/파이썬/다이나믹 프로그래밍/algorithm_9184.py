'''
내용:백준 알고리즘 단계별 풀기 다이나믹 프로그래밍 9184 신나는 함수 실행
날짜:21년2월1일
사용 언어:파이썬
'''
ret_dic = {}

def w(a,b,c):
    if (a,b,c) in ret_dic.keys():
        return ret_dic[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        temp1 = w(a,b,c-1)
        ret_dic[(a,b,c-1)] = temp1
        temp2 = w(a,b-1,c-1)
        ret_dic[(a,b-1,c-1)] = temp2
        temp3 = w(a,b-1,c)
        ret_dic[(a,b-1,c)] = temp3
        return temp1 + temp2 - temp3
    else:
        temp1 = w(a - 1, b, c)
        ret_dic[(a-1, b, c)] = temp1
        temp2 = w(a - 1, b - 1, c)
        ret_dic[(a - 1, b-1, c)] = temp2
        temp3 = w(a - 1, b, c - 1)
        ret_dic[(a - 1, b, c-1)] = temp3
        temp4 = w(a - 1, b-1, c - 1)
        ret_dic[(a - 1, b-1, c-1)] = temp4
        return temp1 + temp2 + temp3 - temp4
inputs =[]
while True:
    x = list(map(int,input().split(' ')))
    if x[0] == -1 and x[1] == -1 and x[2] == -1:
        break
    inputs.append(x)

for input_list in inputs:
    value = w(input_list[0],input_list[1],input_list[2])
    print('w(%d, %d, %d) = %d' %(input_list[0],input_list[1],input_list[2],value))



