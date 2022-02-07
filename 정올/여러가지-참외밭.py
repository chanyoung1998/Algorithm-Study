import sys


n = int(sys.stdin.readline())
lists = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(6)]

h = 0
width = 0
for dir,l in lists:
    if dir == 1:
        width+= l
    elif dir == 3:
        h += l
sum_ = 0

#참회밭의 넓이를 4부분으로 나눌 수 있음
#1 2
#3 4
#예를 들어 ㄱ모양이면 1,2,4번이 참회밭의 총 넓이
#근데 밑에 포문 돌면서 넓이 구하면
#1,2,4,번 구역이 3번// 3번 구역이 2번 더해짐
#총 넓이가 1,2,3,4니까 총 넓이 2번 빼주면
#1,2,4번 넓이만 구할 수 있음



for i in range(6):
    sum_ += lists[i][1] * lists[(i+1)%6][1]

sum_ -= width*h*2
print(sum_*n)