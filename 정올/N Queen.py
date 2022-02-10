import sys
# https://blog.naver.com/PostView.naver?blogId=bccdr&logNo=222383723253&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
n = int(sys.stdin.readline())
board = [-1 for _ in range(n)]
columns = [False for _ in range(n)]
diagonal_up = [False for _ in range(2*n)]
diagonal_down= [False for _ in range(2*n)]
ans = 0
def dfs(row):
    global ans
    if row == n:
        ans += 1
        return

    for i in range(n):

        if columns[i]:
            continue
        if diagonal_up[row-i + n]:
            continue
        if diagonal_down[row+i]:
            continue

        columns[i],diagonal_up[row-i + n],diagonal_down[row+i] = True,True,True
        dfs(row+1)
        columns[i], diagonal_up[row - i + n], diagonal_down[row + i] = False,False,False

    return
dfs(0)
print(ans)