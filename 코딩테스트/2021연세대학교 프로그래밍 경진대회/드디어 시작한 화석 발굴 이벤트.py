import sys

n = int(sys.stdin.readline().rstrip())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
find = [[False for _ in range(n)] for _ in range(n)]
fossil = []

def solve(i,j):
    if (True if j == 0 else maps[i][j-1] == '.') and (True if i == 0 else maps[i-1][j] == '.')  and (False if j +1 >= n else maps[i][j+1] == '.') and (False if j +2>= n  else maps[i][j+2] == '#') and (False if i +1 >= n else maps[i+1][j] == '#'):

        count = 0
        for x in range(n):
            if i + x >= n:
                break
            if maps[i+x][j] == '#':
                count += 1
            elif maps[i+x][j] == '.':
                break
        if count < 5 or count % 4 != 1 :
            return
        for w in range(count):
            for z in range(count):
                find[i+w][j+z] = True
        k = count // 4
        fossil.append(("UL",count, i + 2 * k, j + 2 * k))

    elif (True if j == n-1 else maps[i][j+1] == '.') and (True if i == 0 else maps[i-1][j] == '.')  and (False if j -1 < 0 else maps[i][j-1] == '.') and (False if j -2< 0 else maps[i][j-2] == '#') and (False if i +1 >= n else maps[i+1][j] == '#'):

        count = 0
        for x in range(n):
            if i + x >= n:
                break
            if maps[i+x][j] == '#':
                count += 1
            else:
                break
        if count < 5 or count % 4 != 1:
            return
        for w in range(count):
            for z in range(count):
                find[i+w][j-z] = True
        k = count // 4
        fossil.append(("UR",count, i + 2 * k , j - (2 * k)))

    elif (True if j == 0 else maps[i][j-1] == '.') and (True if i == n-1 else maps[i+1][j] == '.')  and (False if j +1 >= n else maps[i][j+1] == '.') and (False if j +2>= n  else maps[i][j+2] == '#') and (False if i - 1 < 0 else maps[i-1][j] == '#'):

        count = 0
        for x in range(n):
            if i - x < 0:
                break
            if maps[i-x][j ] == '#':
                count += 1
            else:
                break
        if count < 5 or count % 4 != 1:
            return
        for w in range(count):
            for z in range(count):
                find[i-w][j+z] = True
        k = count // 4
        fossil.append(("DL",count, i - (2 * k), j + 2 * k))

    elif (True if j == n-1 else maps[i][j+1] == '.') and (True if i == n-1 else maps[i+1][j] == '.')  and (False if j-1 < 0 else maps[i][j-1] == '.') and (False if j - 2 < 0 else maps[i][j-2] == '#') and (False if i - 1 < 0 else maps[i-1][j] == '#'):

        count = 0
        for x in range(n):
            if i - x < 0:
                break
            if maps[i-x][j] == '#':
                count += 1
            else:
                break
        if count < 5 or count % 4 != 1:
            return
        for w in range(count):
            for z in range(count):
                find[i-w][j-z] = True
        k = count // 4
        fossil.append(("DR",count, i - (2 * k ), j - (2 * k )))

    elif (True if i == 0 else maps[i-1][j] == '.') and (True if j == 0 else maps[i][j-1] == '.')  and (False if i +1 >= n else maps[i+1][j] == '.') and (False if i +2>= n  else maps[i+2][j] == '#') and (False if j +1 >= n else maps[i][j+1] == '#'):

        count = 0
        for x in range(n):
            if j + x >= n:
                break
            if maps[i][j+x] == '#':
                count += 1
            else:
                break
        if count < 5 or count % 4 != 1:
            return
        for w in range(count):
            for z in range(count):
                find[i+w][j+z] = True
        k = count // 4
        fossil.append(("LU",count, i + 2 * k , j + 2 * k))

    elif (True if i == n-1 else maps[i+1][j] == '.') and (True if j == 0 else maps[i][j-1] == '.')  and (False if i -1 < 0 else maps[i-1][j] == '.') and (False if i -2< 0 else maps[i-2][j] == '#') and (False if j +1 >= n else maps[i][j+1] == '#'):

        count = 0
        for x in range(n):
            if j + x >= n:
                break
            if maps[i][j+x] == '#':
                count += 1
            else:
                break
        if count < 5 or count % 4 != 1:
            return
        for w in range(count):
            for z in range(count):
                find[i-w][j+z] = True
        k = count // 4
        fossil.append(("LD",count, i - (2 * k ), j + 2 * k))

    elif (True if i == 0 else maps[i-1][j] == '.') and (True if j == n-1 else maps[i][j+1] == '.')  and (False if i +1 >= n else maps[i+1][j] == '.') and (False if i +2>= n  else maps[i+2][j] == '#') and (False if j - 1 < 0 else maps[i][j-1] == '#'):

        count = 0
        for x in range(n):
            if j - x < 0:
                break
            if maps[i][j-x] == '#':
                count += 1
            else:
                break
        if count < 5 or count % 4 != 1:
            return
        for w in range(count):
            for z in range(count):
                find[i+w][j-z] = True
        k = count // 4
        fossil.append(("RU",count, i + 2 * k , j - (2 * k )))

    elif (True if i == n-1 else maps[i+1][j] == '.') and (True if j == n-1 else maps[i][j+1] == '.')  and (False if i-1 < 0 else maps[i-1][j] == '.') and (False if i - 2 < 0 else maps[i-2][j] == '#') and (False if j - 1 < 0 else maps[i][j-1] == '#'):

        count = 0
        for x in range(n):
            if j - x < 0:
                break
            if maps[i][j-x] == '#':
                count += 1
            else:
                break
        if count < 5 or count % 4 != 1:
            return
        for w in range(count):
            for z in range(count):
                find[i-w][j-z] = True
        k = count // 4
        fossil.append(("RD",count, i - (2 * k), j - 2 * k))


for i in range(n):
    for j in range(n):
        if maps[i][j] == '#' and not find[i][j]:
            solve(i,j)

fossil.sort(key=lambda x:(x[2],x[3]))
print(len(fossil))
for i in range(len(fossil)):
    print(fossil[i][2]+1,fossil[i][3]+1,fossil[i][1],fossil[i][0])
