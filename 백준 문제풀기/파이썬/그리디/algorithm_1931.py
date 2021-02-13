'''
내용:백준 알고리즘 단계별 풀기 그리디 마지막 문제
날짜:21년2월13일
사용 언어:파이썬
'''

n = int(input())
time_tables = []
for i in range(n):
    time_tables.append(list(map(int, input().split())))
time_tables.sort(key = lambda x:(x[1],x[0]))

start_time = time_tables[0][0]
end_time = time_tables[0][1]
count = 1
for i in range(1, len(time_tables)):
    if end_time <= time_tables[i][0]:
        start_time = time_tables[i][0]
        end_time = time_tables[i][1]
        count += 1
print(count)