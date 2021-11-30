

def rotate_matrix(array):

    n = len(array) # 행 길이
    m = len(array[0]) # 열 길이

    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1]  = array[i][j]

    return result

def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n,2 * n):
        for j in range(n, 2 * n):
            if new_lock[i][j] == 1:
                continue
            else:
                return False

    return True


def sol(key,lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0 for _ in range(n * 3)] for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    for rotation in range(4):
        key = rotate_matrix(key)

        for i in range(2 * n):
            for j in range(2 * n):
                for w in range(m):
                    for y in range(m):
                         new_lock[i + w][i + y] += key[w][y]
                if check(new_lock):
                    return True
                else:
                    for w in range(m):
                        for y in range(m):
                            new_lock[i + w][i + y] -= key[w][y]

    return False




