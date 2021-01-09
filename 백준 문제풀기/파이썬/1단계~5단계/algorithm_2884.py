'''
내용:백준 알고리즘 단계별 풀기 if문 2884번 알람 시계
날짜:21년1월6일
사용 언어:파이썬
'''

hour_string,minute_string = input().split()

hour = int(hour_string)
minute = int(minute_string)

if minute >= 45:
    print(hour,minute-45)
else:
    if hour == 0:
        hour =23
        print(hour,60 +(minute - 45))
    else:
        hour = hour-1
        print(hour, 60 + (minute - 45))