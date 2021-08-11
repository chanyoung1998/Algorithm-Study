''' 투포인터 부분을 이분탐색으로 해서 풀 수도 있음
이분 탐색으로 푼 코드
출처 :https://it-ys-jw.tistory.com/39

#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int N;
int hi;
int lo;
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0 ,-1, 0, 1 };
int map[100][100];
bool visited[100][100];
#define INF 1000000000

class node {
public:
    int x;
    int y;
    node() {}
    node(int x, int y) :x(x), y(y) {}
};

bool bfs(int diff) { // 범위 차
    int i;
    int j;
    int k;
    int x;
    int y;
    int nx;
    int ny;

    queue<node> q;
    node tmp;

    for (i = lo; i <= hi; i++) { // lo - hi까지의 범위 내
        memset(visited, true, sizeof(visited));

        for (j = 0; j < N; j++) {
            for (k = 0; k < N; k++) {
                if (map[j][k] >= i && map[j][k] <= i + diff) { // 해당 diff(간격)이 가능한지를 판단
                    visited[j][k] = false;
                }
            }
        }

        tmp.x = tmp.y = 0;
        q.push(tmp);

        while (!q.empty()) { // bfs로 경로있는지 확인
            tmp = q.front(); q.pop();
            x = tmp.x;
            y = tmp.y;

            if (visited[y][x]) continue;
            visited[y][x] = true;

            if (x == N - 1 && y == N - 1) return true; // 경로가 있다면 해당 범위 가능

            for (j = 0; j < 4; j++) {
                nx = dx[j] + x;
                ny = dy[j] + y;

                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    tmp.x = nx;
                    tmp.y = ny;

                    q.push(tmp);
                }
            }
        }
    }

    return false; // 다 돌려봤는데도 없다면 해당 범위는 불가
}

int solve() { // 이분 탐색
    int start = 0;
    int end = hi - lo;
    int mid;

    while (start <= end) { // 간격을 가능한 줄이는 것
        mid = (start + end) / 2;
        if (bfs(mid)) end = mid - 1; // 이 경우는 경로가 있음(대신 간격을 더 좁힐 수 있는지 돌려봄)
        else start = mid + 1; // 해당 값이 경로가 없다면 범위를 더 크게 잡아야됨
    }

    return end + 1;
}

int main() {
    int i;
    int j;
    lo = INF;
    hi = -1;

    memset(visited, false, sizeof(visited));
    scanf("%d", &N);

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            scanf("%d", &map[i][j]);
            if (map[i][j] < lo) lo = map[i][j];
            if (map[i][j] > hi) hi = map[i][j];
        }
    }

    printf("%d\n", solve());

    return 0;
}

'''

import sys
from collections import deque
n = int(sys.stdin.readline())
arrays = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(low,high):
    queue = deque()

    if low <= arrays[0][0] <= high:
        queue.append((0,0))
        visited[0][0] = True
    else:
        return False

    while queue:
        x,y = queue.popleft()

        if x == n-1 and y == n- 1:
            return True

        for dir in range(4):
            p = x + dx[dir]
            q = y + dy[dir]

            if 0 <= p < n and 0 <= q < n and not visited[p][q] and low <= arrays[p][q] <= high:
                queue.append((p,q))
                visited[p][q] = True


    return False


maxv = -sys.maxsize
minv = sys.maxsize
for i in range(n):
    for j in range(n):
        maxv = max(maxv,arrays[i][j])
        minv = min(minv,arrays[i][j])

ret = sys.maxsize
end = 0
for start in range(0,maxv+1):

    while end <= maxv:
        visited = [[False] * n for _ in range(n)]
        if bfs(start,end):
            if start == 0 and end == 0:
                print(0)
                exit(0)
            ret = min(end - start, ret)
            break
        else:
            end += 1

print(ret)