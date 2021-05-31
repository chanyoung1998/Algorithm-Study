'''
내용:백준 알고리즘 1439 이코테 문자열 뒤집기
날짜:21년5월31일
사용 언어:파이썬
'''

import sys

s = list(map(int,sys.stdin.readline().rstrip()))



if len(s) == 1:
    print(0)
else:
    prev = s[0]
    count_zero = 0
    count_one = 0

    if s[0] == 1:
        count_one = 1
    else:
        count_zero = 1

    for i in s[1:]:
        if prev == i:
            continue
        else:
            prev = i
            if i == 1:
                count_one += 1
            else:
                count_zero += 1

    print(min(count_zero,count_one))

