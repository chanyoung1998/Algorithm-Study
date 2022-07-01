import sys

n = int(sys.stdin.readline())
point = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
point.sort(key= lambda x: (x[0],x[1]))
min_distance = sys.maxsize
def distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)

def DNQ(s,e):
    global min_distance
    if e-s <= 2:
        if e-s == 2:
            min_distance = min(min_distance,distance(point[s],point[s+1]),distance(point[s+1],point[e]),distance(point[s],point[e]))
        elif e-s == 1:
            min_distance = min(min_distance,distance(point[s],point[e]))

        return


    m = (s+e)//2

    CPL = DNQ(s,m)
    CPR = DNQ(m+1,e)


    temp = []
    for i in range(s,e+1):
        if (point[i][0] - point[m][0])**2 <= min_distance:
            temp.append((point[i][0],point[i][1]))



    temp.sort(key=lambda x: x[1])
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if temp[j][1]-temp[i][1] > min_distance or j >= i +7:
                break
            if j < i+7:
                min_distance = min(min_distance,distance(temp[i],temp[j]))
    return



DNQ(0,n-1)
print(min_distance)
