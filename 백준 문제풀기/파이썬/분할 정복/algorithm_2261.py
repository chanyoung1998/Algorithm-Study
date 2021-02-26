'''
내용:백준 알고리즘 단계별 풀기 분할 정복 2261 가장 가까운 두점
날짜:21년2월25일
사용 언어:파이썬
'''
import sys
def distance(p1,p2):
    x_d = (p1[0]-p2[0]) ** 2
    y_d =(p1[1] - p2[1]) ** 2
    return (x_d + y_d)


def sol(start,end):
    global min_distance
    if start == end:
        return
    elif end - start == 1:
        min_distance = min(min_distance, distance(points[start],points[end]))
        return

    mid = (start+end) // 2
    sol(start, mid)
    sol(mid+1, end)

    mid_x = (points[mid][0]+points[mid-1][0])//2
    temp = []
    for i in range(start,end+1):
        if (points[i][0]- mid_x)**2 <= min_distance:
            temp.append(points[i])

    #y축을 기준으로 정렬
    temp.sort(key=lambda x: x[1])
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if j < i+7:
                min_distance = min(min_distance,distance(temp[i],temp[j]))
    return


n = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
points.sort(key= lambda x : x[0])
min_distance = sys.maxsize
sol(0,n-1)
print(min_distance)
