'''
내용:백준 알고리즘 단계별 풀기 1차원 배열 4344번 평균은 넘겠지
날짜:21년1월8일
사용 언어:파이썬
'''

C = int(input())
N_list = []
count = 0
for i in range(C):
    N_list.append(list(map(int,input().split(' '))))

for i in range(C):
    a = (sum(N_list[i])-N_list[i][0])
    b = N_list[i][0]
    avg = a/b
    for j in range(1,len(N_list[i])):
        if(N_list[i][j]>avg):
            count = count +1

    print(format(count/b*100,'.3f'),"%",sep='')
    count = 0


'''
파이썬은 반올림을 하는 round() 함수를 내장하고 있습니다.
그러나 round() 함수는 끝자리가 0이면 출력을 하지 않는 문제가 있습니다.
예컨대 round(3.141592, 2)는 3.14를 출력하지만, round(3.101592, 2)는 3.1을 출력합니다.
참고로 올림 또는 내림을 하는 math.ceil과 math.floor은 정수만 반환합니다.
따라서 원하는 출력형식을 엄격하게 준수하려면 format() 함수를 사용해야 합니다.
format() 함수는 format(item, 폭(width).정밀도(precision)f)의 형태로 사용하면 됩니다.
즉 format(3.141592, ".2f"))의 형식으로 소수점 두 자리까지 출력할 수 있습니다.
한편 "{:.1f}".format() 형태로도 사용할 수 있습니다.
'''