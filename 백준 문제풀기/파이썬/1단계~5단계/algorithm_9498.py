'''
내용:백준 알고리즘 단계별 풀기 if문 9498번 시험 성적
날짜:21년1월6일
사용 언어:파이썬
'''

grade_string = input()
grade = int(grade_string)
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

