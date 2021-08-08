# 0808
# 인구 이동
# idea: bfs, 완전 탐색

import sys
from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인구 이동 후 결과 반환 함수
def bfs(i, j):
    global check
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visted[nx][ny] and l <= abs(board[nx][ny] - board[x][y]) <= r:
                visted[nx][ny] = True
                q.append([nx, ny])
                temp.append([nx, ny])

    if len(temp) > 1:
        check = True
        num = sum(board[x][y] for x, y in temp) // len(temp)
        for x, y in temp:
            board[x][y] = num

if __name__ == "__main__":
    n, l, r = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans = 0
    while True:
        # 인구이동 할때마다 방문하지 않은 리스트 초기화
        visted = [[False] * n for _ in range(n)]
        check = False
        for i in range(n):
            for j in range(n):
                if not visted[i][j]:
                    visted[i][j] = True
                    bfs(i, j)
        if not check:
            break
        ans += 1

    print(ans)