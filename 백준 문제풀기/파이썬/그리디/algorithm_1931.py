n = int(input())
time_tables = []
count = 0
for i in range(n):
    time_tables.append(list(map(int,input().split())))
time_tables.sort(key= lambda x: (x[0],x[1]))

start = 0
end = 0
time = 0

while i < len(time_tables):
    for j in range(i+1,len(time_tables)):
        if time_tables[j][0] <= time_tables[i][0]:
            pass




    start = time_tables[i][0]
    end = time_tables[i][1]
    time = end - start
    i += 1

