'''
21.05.04
문자열 및 분할 정복
정답 여부 : 한번에 통과
'''
import sys
from itertools import combinations
numbers = list(map(int,sys.stdin.readline().rstrip()))
length = len(numbers)
ret = []
def oddholic(numbers,length,count):

    if length == 1:
        if numbers[0] % 2 == 0:
            return ret.append(count)
        else:
            return ret.append(count + 1)
    elif length == 2:
        for i in numbers:
            if i % 2 == 1:
                count += 1
        temp = sum(numbers)
        new_numbers = list(map(int,str(temp)))
        oddholic(new_numbers,len(new_numbers),count)
    else:
        for i in numbers:
            if i % 2 == 1:
                count += 1
        comb = list(combinations(range(1,length),2))

        for i,j in comb:
            #print(numbers[:i], numbers[i:j], numbers[j:])

            temp1 = ''
            for k in numbers[:i]:
                temp1 += str(k)
            temp1 = int(temp1)

            temp2 =''
            for k in numbers[i:j]:
                temp2 += str(k)
            temp2 = int(temp2)

            temp3 = ''
            for k in numbers[j:]:
                temp3 += str(k)
            temp3 = int(temp3)
            #print(temp1,temp2,temp3,sep='/')
            new_numbers = list(map(int,str(temp1+temp2+temp3)))
            oddholic(new_numbers,len(new_numbers),count)

oddholic(numbers,len(numbers),0)

print(min(ret),max(ret),sep=' ')











